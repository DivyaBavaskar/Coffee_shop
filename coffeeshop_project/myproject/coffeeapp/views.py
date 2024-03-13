from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Coffee,Cartitem,Customer1
from django.contrib.auth.forms import  UserCreationForm
# Create your views here.

def FirstPage(request):
    return render(request,'Firstpage.html')
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')
        
#         if pass1!=pass2:
#             return HttpResponse("Your password and confirm password are not same!! ")
#         else:
             
#              my_user=User.objects.create_user(uname,email,pass1)
#              my_user.save()
#              return redirect('login')

# from django.db import IntegrityError

# def SignupPage(request):
#     if request.method == 'POST':
#         uname = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')

#         if pass1 != pass2:
#             return HttpResponse("Your password and confirm password are not the same!!")
#         else:
#             try:
#                 my_user = User.objects.create_user(uname, email, pass1)
#                 my_user.save()
#                 return redirect('login')
#             except IntegrityError:
#                 return HttpResponse("Username already exists. Please choose a different one.")

#     return render(request, 'signup.html')

def signup(request):
    if request.method=='POST':
        fn=UserCreationForm(request.POST)
        if fn.is_valid():
            u = fn.save()
            cus = Customer1.objects.create(user=u)
            print(cus)
            return redirect('/login')
    else:
        fn=UserCreationForm()
    return render(request,'signup.html',{'form':fn})

    

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass') 
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")

    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def HomePage(request):
    coffee = Coffee.objects.all()
    return render(request,'home.html',{'coffee': coffee})

def coffee_detail(request,id):
    idd=Coffee.objects.get(id=id)
    return render(request,'coffeedetail.html',{'data':idd})

def add(request):
    data={

    }
    try:
        if request.method == "POST":
            num1=request.POST.get('num1')
            num2=request.POST.get('num2')
            num=num1+num2
            print(num1)
            data={
                "num":num
            }
            print(num)
    except:
        pass
    return render(request,'coffeeapp/add.html',data)

from django.views.generic import ListView
from django.db.models import Q
class SearchResultsView(ListView):
    model=Coffee
    template_name='search_results.html'
    def get_queryset(self):
        query=self.request.GET.get('q')
        object_List= Coffee.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(image__icontains=query)|Q(price__icontains=query))
        return object_List
    
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=order.objects.get_or_create(customer=customer,complete=True)
        print(order)
        print(created)
        items=order.orderitem_set.all()
    
        print(items)
    else:
        items=[]
    context={'items':items,'order':order}
    return render(request,'petsapp/cart.html',context)

def checkout(request):
    return render(request,'petsapp/checkout.html')

def checkout(request):
	context={}
	return render(request,'petsapp/checkout.html',context)


def add_to_cart(request,coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    customer=Customer1.objects.get(user=request.user)
    existing_cart_items=Cartitem.objects.filter(customer=customer,coffee=coffee)
    if len(existing_cart_items)==0:
        cart_item=Cartitem.objects.create(customer=customer,coffee=coffee)
    else:
        cart_item=existing_cart_items[0]
    cart_item.quantity=request.POST['quantity']
    cart_item.save()
    return redirect('cart_items')


def collect_cart_details(request):
    cart_items_list=Cartitem.objects.filter(customer__user=request.user)
    qty_list=[n for n in range(1,6)]
    all_items_price=0
    for item in cart_items_list:
        item.item_price=item.quantity*item.coffee.price
        all_items_price=all_items_price+item.item_price
    context={
        'cart':cart_items_list,
        'total_price':all_items_price,
        'qty_list':qty_list
    }
    return context

def cart_items(request):
    context = collect_cart_details(request)
    return render(request,'cart_items.html',context=context)
    

def remove_from_cart(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    cart_item = Cartitem.objects.get(customer__user=request.user.id, coffee=coffee)
    cart_item.delete()
    return redirect('cart_items')

from .forms import ShippingAddress1Form
def add_address(request):
    if request.method == 'POST':
        form = ShippingAddress1Form(request.POST)
        if form.is_valid():
            sd = form.save(commit=False)
            sd.customer = Customer1.objects.get(id=request.POST['customer'])
            sd.save()
            return redirect('list_address')
    else:
        form = ShippingAddress1Form()
    return render(request, 'coffeeapp/add_address.html', {'form': form})









