from django.shortcuts import render

# Create your views here.
def cart_detail(request):
    """ A view that renders the cart contents"""

    return render(request, 'cart/cart.html')