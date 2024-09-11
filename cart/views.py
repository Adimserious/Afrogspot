from django.shortcuts import render, redirect

# Create your views here.
def cart_detail(request):
    """ A view that renders the cart contents"""

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
