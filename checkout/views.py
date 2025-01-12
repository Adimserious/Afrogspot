from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
from profiles.forms import ProfileForm
from profiles.models import Profile
from .models import Order, OrderItem, Product, ProductVariant
from decimal import Decimal
from django.utils import timezone
from paypalrestsdk import Payment
import checkout.paypal_config
import stripe



stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    # Get the cart from session
    cart = request.session.get('cart', {})

    # Check if cart is empty
    if not cart:
        messages.error(
            request,
            'Your cart is empty. Please add items to your cart before proceeding to checkout.'
        )
        return redirect('cart_detail')

    # Calculate order total
    order_total = calculate_order_total(request)

    # Condition to determine if free delivery should be applied
    free_delivery_threshold = 50  # Free delivery on orders above €50
    if order_total >= free_delivery_threshold:
        delivery_cost = Decimal('0.00')  # Free delivery
    else:
        delivery_cost = Decimal('7.00')  # Standard delivery cost

    grand_total = order_total + delivery_cost

    # Creates PaymentIntent
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(grand_total * 100),  # Convert to cents
            currency='eur',
        )
        client_secret = intent.client_secret
        payment_intent_id = intent.id
    except stripe.error.StripeError as e:
        messages.error(request, f'Error with Stripe: {str(e)}')
        return redirect('cart_detail')

    # PayPal Payment Creation
    paypal_payment = Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
        "return_url": request.build_absolute_uri(reverse('execute_payment')),
        "cancel_url": request.build_absolute_uri(reverse('cancel_payment')),
        },
        "transactions": [{
            "item_list": {
                "items": [
                    {
                        "name": "Order Payment",
                        "sku": "ORDER001",
                        "price": f"{grand_total:.2f}",
                        "currency": "EUR",
                        "quantity": 1,
                    }
                ]
            },
            "amount": {
                "total": f"{grand_total:.2f}",
                "currency": "EUR",
            },
            "description": "Payment for your order.",
        }],
    })

    try:
        if paypal_payment.create():
            paypal_approval_url = next(link.href for link in paypal_payment.links if link.rel == "approval_url")
        else:
            messages.error(request, "Error creating PayPal payment.")
            paypal_approval_url = None
    except Exception as e:
        messages.error(request, f"PayPal error: {str(e)}")
        paypal_approval_url = None


    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # The payment has been confirmed on the client-side; creates the order
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.order_total = order_total
            order.delivery_cost = delivery_cost
            order.grand_total = grand_total

            # Identify the selected payment method
            payment_method = request.POST.get('payment_method')  # Example: form field or dropdown
            if payment_method == 'stripe':
                # Store Stripe-specific details and mark the order as pending
                order.stripe_payment_intent = payment_intent_id
                order.payment_method = 'stripe'
                order.payment_status = 'pending'
                order.save()
                process_cart_items(cart, order)

                # Proceed with Stripe payment processing
                handle_payment_success(request, order, 'stripe', payment_intent_id)
                # Clear the cart only after everything is confirmed
                request.session['cart'] = {}
                request.session.modified = True
                return redirect('order_confirmation', order_id=order.id)

            elif payment_method == 'paypal':
                # Save order as pending for now (to be finalized in `execute_payment`)
                order.payment_method = 'paypal'
                order.payment_status = 'pending'
                order.paypal_payment_id = paypal_payment.id  # Save PayPal payment ID
                order.save()
                process_cart_items(cart, order)

                # Redirect user to PayPal for approval
                if paypal_approval_url:
                    return redirect(paypal_approval_url)
                else:
                    messages.error(request, "An error occurred while creating the PayPal payment.")
                    return redirect('cart_detail')

            else:
                messages.error(request, "Invalid payment method selected.")
                return redirect('cart_detail')
        
            # Create order items and reduce stock
            for key, item_data in cart.items():
                if isinstance(item_data, dict):
                    product = get_object_or_404(Product, id=item_data['product_id'])
                    variant = None

                    # Check if the item is a variant
                    if item_data.get('variant_id'):
                        variant = get_object_or_404(ProductVariant, id=item_data['variant_id'])

                        # Check if enough stock is available for the variant
                        if variant.stock >= item_data['quantity']:
                            variant.stock -= item_data['quantity']  # Reduce stock
                            variant.save()
                        else:
                            messages.error(
                                request,
                                f'Sorry, only {variant.stock} of {product.name} (variant) is available.'
                            )
                            return redirect('cart_detail')
                    else:
                        # Check if enough stock is available for the product
                        if product.stock >= item_data['quantity']:
                            product.stock -= item_data['quantity']  # Reduce stock
                            product.save()
                        else:
                            messages.error(
                                request,
                                f'Sorry, only {product.stock} of {product.name} is available.'
                            )
                            return redirect('cart_detail')
                

                    # Create the order item after checking stock
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        variant=variant,
                        quantity=item_data['quantity'],
                        price=Decimal(item_data['price'])
                    )

            
            # Saves user info if `save_info` is checked
            save_info = form.cleaned_data.get('save_info')
            if save_info and request.user.is_authenticated:
                profile = request.user.profile
                profile.full_name = form.cleaned_data['full_name']
                profile.email = form.cleaned_data['email']
                profile.phone_number = form.cleaned_data['phone_number']
                profile.address_line_1 = form.cleaned_data['address_line_1']
                profile.address_line_2 = form.cleaned_data['address_line_2']
                profile.city = form.cleaned_data['city']
                profile.postal_code = form.cleaned_data['postal_code']
                profile.country = form.cleaned_data['country']
                profile.save()

                # Call handle_payment_success
                handle_payment_success(request, order, 'stripe', payment_intent_id)
                return redirect('order_confirmation', order_id=order.id)

            # Order confirmation email
            send_order_confirmation_email(order)

            messages.success(request, 'Your order has been placed successfully!')
            return redirect('order_confirmation', order_id=order.id)

    else:
        # If the user is authenticated, prefill the form with their profile information
        if request.user.is_authenticated:
            profile = request.user.profile
            initial_data = {
                'full_name': profile.default_full_name,
                'email': profile.default_email,
                'phone_number': profile.default_phone_number,
                'address_line_1': profile.default_address_line_1,
                'address_line_2': profile.default_address_line_2,
                'city': profile.default_city,
                'postal_code': profile.default_postal_code,
                'country': profile.default_country,
            }
        form = CheckoutForm(initial=initial_data if request.user.is_authenticated else None)

    context = {
        'form': form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': client_secret,
        'order_total': order_total,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
        'paypal_client_id': settings.PAYPAL_CLIENT_ID,  
        'currency_code': 'EUR',
        
    }

    return render(request, 'checkout/checkout.html', context)



def handle_payment_success(request, order, payment_method, payment_id=None):
    """
    Handles the logic after a successful payment.
    - Marks the order as paid.
    - Stores payment details.
    - Sends a confirmation email.
    """
    order.payment_method = payment_method
    if payment_method == 'stripe':
        order.stripe_payment_intent = payment_id
    elif payment_method == 'paypal':
        order.paypal_payment_id = payment_id
    order.payment_status = 'completed'
    order.save()

    # Send order confirmation email
    send_order_confirmation_email(order)

    # Notify user of successful order placement
    messages.success(
        request,
        f'Payment successful! Your order #{order.order_number} has been placed.'
    )


# paypal
def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    if not payment_id or not payer_id:
        messages.error(request, "Missing payment details.")
        return redirect('cart_detail')

    try:
        payment = Payment.find(payment_id)
        existing_order = Order.objects.filter(paypal_payment_id=payment_id, payment_status='completed').first()
        if existing_order:
            messages.info(request, "This payment has already been processed.")
            return redirect('order_confirmation', order_id=existing_order.id)

        if payment.execute({"payer_id": payer_id}):
            order = get_object_or_404(Order, paypal_payment_id=payment_id)
            handle_payment_success(request, order, 'paypal', payment_id)
            # Clear the cart only after everything is confirmed
            request.session['cart'] = {}
            request.session.modified = True
            return redirect('order_confirmation', order_id=order.id)
        else:
            messages.error(request, "Payment failed. Please try again.")
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")

    return redirect('cart_detail')

# paypal
def cancel_payment(request):
    messages.info(request, "You have canceled the payment.")
    return redirect('cart_detail')


def process_payment(order, payment_method, payment_id=None):
    """
    Process the payment for an order.
    Marks the order as paid, saves payment details, and sends an email.
    """
    order.payment_method = payment_method
    order.payment_status = 'completed'
    if payment_method == 'stripe':
        order.stripe_payment_intent = payment_id
    elif payment_method == 'paypal':
        order.paypal_payment_id = payment_id
    order.save()

    send_order_confirmation_email(order)
    return True

def process_cart_items(cart, order):
    for key, item_data in cart.items():
        product = get_object_or_404(Product, id=item_data['product_id'])
        variant = None
        if item_data.get('variant_id'):
            variant = get_object_or_404(ProductVariant, id=item_data['variant_id'])
            if variant.stock < item_data['quantity']:
                raise ValueError(f"Insufficient stock for variant {variant.id}")
            variant.stock -= item_data['quantity']
            variant.save()
        else:
            if product.stock < item_data['quantity']:
                raise ValueError(f"Insufficient stock for product {product.id}")
            product.stock -= item_data['quantity']
            product.save()
        OrderItem.objects.create(order=order, product=product, variant=variant, quantity=item_data['quantity'], price=item_data['price'])
    order.save()


def send_order_confirmation_email(order):
    # Check if the environment is production or development
    if settings.DEBUG:
        print(f"Customer Email: {order.email}")
        print(f"Order Confirmation for Order #{order.id}")
        return  # Do not send the email in development

    subject = f'Order Confirmation - Order #{order.id}'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [order.email]
    admin_email = ['lilianadimchinobi@gmail.com']

    # Context for email templates
    context = {
        'order': order,
        'site_name': 'Afrogspot',
        'current_year': timezone.now().year,
        'support_email': 'help.afrogspot@gmail.com',
    }

    try:
        # Render and send customer email
        html_message = render_to_string('checkout/order_email_confirmation.html', context)
        plain_message = strip_tags(html_message)
        send_mail(
            subject,
            plain_message,
            from_email,
            to_email,
            html_message=html_message,
            fail_silently=False,
        )

        # Notify admin
        admin_subject = f'New Order Notification - Order #{order.id}'
        admin_message = f'Order #{order.id} has been placed by {order.email}.'
        send_mail(
            admin_subject,
            admin_message,
            from_email,
            admin_email,
            fail_silently=False,
        )

    except Exception as e:
        # Log error for debugging
        print(f"Failed to send email: {e}")


# Function to test email sending
def test_email():
    send_mail(
        'Test Email Subject',
        'This is a test email body.',
        'afrogspot@gmail.com',
        ['lilianadimchinobi@gmail.com'],
        fail_silently=True,  # Don't raise an error if sending fails
    )



def calculate_order_total(request):
    cart = request.session.get('cart', {})
    total = Decimal(0)
    for item_data in cart.values():
        if isinstance(item_data, dict):
            price = Decimal(item_data['price'])
            quantity = item_data['quantity']
            total += price * quantity
    return total


def order_confirmation(request, order_id):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, id=order_id)
    return render(
        request,
        'checkout/order_confirmation.html',
        {'order': order}
    )


@login_required
def order_history(request):
    # Retrieve orders for the current user
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    
    context = {
        'orders': orders,
    }
    return render(request, 'checkout/order_history.html', context)


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    # Pass total calculation to context
    for item in order_items:
        item.total_price = item.price * item.quantity

    context = {
        'order': order,
        'order_items': order_items,
        'delivery_cost': order.delivery_cost,  # Adds delivery cost
        'grand_total': order.grand_total,      # Adds grand total
    }
    return render(request, 'checkout/order_detail.html', context)
