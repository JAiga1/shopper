from .models import Product, Category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'shop/product_list.html', {'products': products})

from django.shortcuts import render
from .models import Product

def product_list(request):
    """ View to display and filter products """
    products = Product.objects.all()

    search_query = request.GET.get('search', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort_option = request.GET.get('sort')

    if search_query:
        products = products.filter(title__icontains=search_query)

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    if sort_option == 'price_low':
        products = products.order_by('price')
    elif sort_option == 'price_high':
        products = products.order_by('-price')

    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')  

     
        if not (title and description and price and stock and image and category_id):
            return render(request, 'shop/add_product.html', {
                'error': 'All fields are required!',
                'categories': Category.objects.all()
            })

       
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return render(request, 'shop/add_product.html', {
                'error': 'Invalid Category',
                'categories': Category.objects.all()
            })


        product = Product.objects.create(
            title=title,
            description=description,
            price=price,
            stock=stock,
            image=image,
            category=category
        )
        print(f"✅ Product Added: {product}")  
        return redirect('product_list')

    return render(request, 'shop/add_product.html', {'categories': Category.objects.all()})

@login_required  
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    

    cart, created = Cart.objects.get_or_create(user=request.user)

  
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')  

@login_required
def cart_view(request):
    """ View to display all items in the user's cart """
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'shop/cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, item_id):
    """ View to remove an item from the cart """
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_view')

from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'shop/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')

    return render(request, 'shop/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
