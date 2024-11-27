from django.shortcuts import render,get_object_or_404,redirect

from . models import Product
from . models import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

   pro=Product.objects.all()
  
   return render(request,'home.html',{'pro':pro})

@login_required
def add_to_cart(request,product_id):
   product = get_object_or_404(Product, id=product_id)
   cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
   if not created:
        cart_item.quantity += 1
        cart_item.save()
   return redirect('cart')

login_required
def cart(request):
   total=0
   cart_items = Cart.objects.filter(user=request.user)
   for item in cart_items:
        item.subtotal = item.product.price * item.quantity
        total += item.subtotal
   return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})  

