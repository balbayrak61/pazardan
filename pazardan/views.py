from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout
from.models import Product,Category,Cart,CartItem,Order,OrderItem
from.forms import OrderForm,ProductForms,CustomUserCreationForm, AuthenticationForm,CategoryForm

import logging
logger=logging.getLogger(__name__)

def product_list(request):
    products=Product.objects.all()

    return render(request,'pazardan/product_list.html', {'products': products})

def product_list_by_category(request, category_id):

    category=get_object_or_404(Category,id=category_id)
    products= category.products.filter(available=True)
    return render(request,'pazardan/product_list.html',{'category':category,'products':products})

def product_detail(request,id):
    product=get_object_or_404(Product,id=id,available=True)
    
    return render(request,'pazardan(product_detail.html)',{'product':product})

def add_product(request):
    if request.method == 'POST':
        form= ProductForms(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            messages.success(request,'Ürün başarıyla eklenmiştir.')
            return redirect('product_list')
        else:
            messages.error(request,'Ürün eklenememiştir,Lütfen tekrar seçim yapınız.')
    else:
        form=ProductForms()
        return render(request,'pazardan/add_product.html',{'form':form})
    
def product_delate(request,id):
    product=get_object_or_404(product,id=id)
    if request.method == 'POST':
        product.delate()
        return redirect('product_list')
    return redirect ('product_list')

def add_category(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Kategori başarıyla eklendi.')
            return redirect('product_list')
    else:
        form=CategoryForm()
    return render(request,'pazardan/add_category.html',{'form': form})

def cart_detail(request):
    cart,created= Cart.objects.get_or_create(session_key=request.session.session_key)
    return render (request,'pazardan/cart_detail.html',{'cart':cart})

def cart_add(request,product_id):
    cart,created= Cart.objects.get_or_create(session_key=request.session.session_key)
    product=get_object_or_404(Product,id=product_id)
    cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)
    cart_item.save()
    messages.success(request,'ürün karta başarılı bir şekilde eklendi')

    return redirect('cart_detail')


def cart_remove(request,product_id):
    cart=Cart.objects.get(session_key=request.session.session_key)
    product=get_object_or_404(Product,id=product_id)
    cart_item=get_object_or_404(CartItem,cart=cart,product=product)
    cart_item.delate()
    messages.success(request,'Ürün karttan başarılı bir şekilde çıkartıldı.')
    return redirect('cart_detail')

def cart_update(request):
    if request.method=='POST':
        cart=Cart.objects.get(session_key=request.session.session_key)
        for key , value in request.POST.items():
            if key.startswith('quantity_'):
                product_id=key.split('_')[1]
                quantity=int(value)
                product=get_object_or_404(Product, id=product_id)
                cart_item,creared=CartItem.objects.get_or_create(cart=cart,product=product)
                cart_item.quantity=quantity
                cart_item.save()
                messages.success(request, f'{product.name} ürünü güncellendi.')
        return redirect('cart_detail')
    return redirect('cart_detail')


def checkout(request):
    try:
        cart=Cart.objects.get(session_key=request.session.session_key)
    
    except Cart.DoesNotExist:
        messages.error(request,'Sepette ürün bulunamadı. Lütfen ürünü tekrar ekleyin. ')

        return redirect('cart_detail')

    if request.mothod== 'POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.cart=cart
            order.paid_amount=sum(item.product.price * item.quantity for item in cart.items.all())
            order.save()


            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
            

            messages.success(request,' Siparişiniz başarılı bir şekilde oluşturuldu.')
            return redirect('orders_list')
        

        else:
            messages.error(request,'Siparişiniz oluşturulamadı. Lütfen tekrar deneyiniz.')
            
    else:
        form=OrderForm()
    
    return render(request,'pazartdan/checkout.html',{'cart': cart, 'form':form})


def orders_list(request):
        orders=Order.objects.prefetch_related('items__product').all()

        return render(request,'pazardan/orders_list.html', {'orders':orders})



def register(request):
    form=CustomUserCreationForm(request.POST)
    if form.is_valid():
        user=form.save()
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password1')
        user=authenticate(username=username,password=password)
        if user is not None:

            auth_login(request,user)
            messages.success(request,f'hoşgeldin {username}')
            return redirect('product_list')
    else:
        form=CustomUserCreationForm
    return render(request,'pazardan/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            auth_login(request,user)
            username=user.username
            messages.success(request,f'hoşgeldin {username}')
            return redirect('product_list')
        else:
            messages.error(request,'Kullanıcı adı veya şifre hatalı.')
    else:
        form=AuthenticationForm()
        return render (request,'pazardan/login.html', {'form':form})

@login_required

def logout_view(request):
    logout(request)
    messages.info(request,'Çıkış yaptınız. ')
    return redirect('product_list')




        

    