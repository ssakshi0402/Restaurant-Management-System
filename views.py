from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import URF, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

def home(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/home.html',{'totalitem':totalitem})
 
class FineView(View):
    def get(self, request):
        Fine_Dining = Product.objects.filter(category='Fine Dining')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/fine.html',{'Fine_Dining':Fine_Dining, 'totalitem':totalitem})

class CasualView(View):
    def get(self, request):
        Casual_Dining = Product.objects.filter(category='Casual Dining')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/casual.html',{'Casual_Dining':Casual_Dining, 'totalitem':totalitem})

class ContView(View):
    def get(self, request):
        Contemporary_Casual = Product.objects.filter(category='Contemporary Casual')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/cont.html',{'Contemporary_Casual':Contemporary_Casual, 'totalitem':totalitem})

class FamilyView(View):
    def get(self, request):
        Family_Style = Product.objects.filter(category='Family Style')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/family.html',{'Family_Style':Family_Style, 'totalitem':totalitem})

class FastView(View):
    def get(self, request):
        Fast_Casual = Product.objects.filter(category='Fast Casual')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/fast.html',{'Fast_Casual':Fast_Casual, 'totalitem':totalitem})

class FastfoodView(View):
    def get(self, request):
        Fast_Food = Product.objects.filter(category='Fast Food')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/fastfood.html',{'Fast_Food':Fast_Food, 'totalitem':totalitem})

class CafeView(View):
    def get(self, request):
        Cafe = Product.objects.filter(category='Cafe')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/cafe.html',{'Cafe':Cafe, 'totalitem':totalitem})

class BuffetView(View):
    def get(self, request):
        Buffet = Product.objects.filter(category='Buffet')
        totalitem = 0
        Buff = Restaurant.objects.filter(Restaurant_category='Buffet')
        one  = 0
        add = None
        if request.user.is_authenticated:
            add = Customer.objects.filter(user=request.user)
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/buffet.html',{'Buffet':Buffet, 'totalitem':totalitem, 'Buff':Buff, 'add':add,'one':one})

class TrucksView(View):
    def get(self, request):
        Food_Trucks_and_Concession_Stands = Product.objects.filter(category='Food Trucks and Concession Stands')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/truck.html',{'Food_Trucks_and_Concession_Stands':Food_Trucks_and_Concession_Stands, 'totalitem':totalitem})

class PopView(View):
    def get(self, request):
        Pop_Up_Restaurant = Product.objects.filter(category='Pop-Up Restaurant')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/pop.html',{'Pop_Up_Restaurant':Pop_Up_Restaurant, 'totalitem':totalitem})


class RestroView(View):
    def get(self, request):
        Fine_Dining = Restaurant.objects.filter(Restaurant_category='Fine Dining')
        Casual_Dining = Restaurant.objects.filter(Restaurant_category='Casual Dining')
        Contemporary_Casual = Restaurant.objects.filter(Restaurant_category='Contemporary Casual')
        Family_Style = Restaurant.objects.filter(Restaurant_category='Family Style')
        Fast_Casual = Restaurant.objects.filter(Restaurant_category='Fast Casual')
        Fast_Food = Restaurant.objects.filter(Restaurant_category='Fast Food')
        Cafe = Restaurant.objects.filter(Restaurant_category='Cafe')
        Buffet = Restaurant.objects.filter(Restaurant_category='Buffet')
        Food_Trucks_and_Concession_Stands = Restaurant.objects.filter(Restaurant_category='Food Trucks and Concession Stands')
        Pop_Up_Restaurant = Restaurant.objects.filter(Restaurant_category='Pop-Up Restaurant')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/res.html',{'Fine_Dining':Fine_Dining,'Casual_Dining':Casual_Dining,
        'Contemporary_Casual':Contemporary_Casual,'Family_Style':Family_Style,'Fast_Casual':Fast_Casual,'Fast_Food':Fast_Food,
        'Cafe':Cafe,'Buffet':Buffet,'Food_Trucks_and_Concession_Stands':Food_Trucks_and_Concession_Stands,
        'Pop_Up_Restaurant':Pop_Up_Restaurant, 'totalitem':totalitem})


class RestrotypeView(View):
    def get(self, request):
        Fine_Dining = Restauranttype.objects.filter(Restaurant_type='Fine Dining')
        Casual_Dining = Restauranttype.objects.filter(Restaurant_type='Casual Dining')
        Contemporary_Casual = Restauranttype.objects.filter(Restaurant_type='Contemporary Casual')
        Family_Style = Restauranttype.objects.filter(Restaurant_type='Family Style')
        Fast_Casual = Restauranttype.objects.filter(Restaurant_type='Fast Casual')
        Fast_Food = Restauranttype.objects.filter(Restaurant_type='Fast Food')
        Cafe = Restauranttype.objects.filter(Restaurant_type='Cafe')
        Buffet = Restauranttype.objects.filter(Restaurant_type='Buffet')
        Food_Trucks_and_Concession_Stands = Restauranttype.objects.filter(Restaurant_type='Food Trucks and Concession Stands')
        Pop_Up_Restaurant = Restauranttype.objects.filter(Restaurant_type='Pop-Up Restaurant')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/restype.html',{'Fine_Dining':Fine_Dining,'Casual_Dining':Casual_Dining,
        'Contemporary_Casual':Contemporary_Casual,'Family_Style':Family_Style,'Fast_Casual':Fast_Casual,'Fast_Food':Fast_Food,
        'Cafe':Cafe,'Buffet':Buffet,'Food_Trucks_and_Concession_Stands':Food_Trucks_and_Concession_Stands,
        'Pop_Up_Restaurant':Pop_Up_Restaurant, 'totalitem':totalitem})

#def product_detail(request):
 #return render(request, 'app/productdetail.html')
 
class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        item_is_in_cart = False
        totalitem = 0
        if request.user.is_authenticated:
            item_is_in_cart = cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/productdetail.html',{'product':product, 'item_is_in_cart':item_is_in_cart, 'totalitem':totalitem})

def add_to_cart(request):
    if request.user.is_authenticated:
        totalitem = 0
        user=request.user
        product_id = request.GET.get('prod_id')
        unique = True
        product = Product.objects.get(id=product_id)
        cart(user=user, product=product).save()
        totalitem = len(cart.objects.filter(user=request.user))
        return redirect('/cart')
    else:
        return redirect('/accounts/login')

def show_cart(request):
    if request.user.is_authenticated:
        totalitem = 0
        user = request.user
        Cart = cart.objects.filter(user=user)
        amount = 0.0
        shipping = 50.0
        wshiping = 0.0
        totalamount = 0.0
        fix = 0.0
        cart_product = [p for p in cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.disc_price)
                amount += tempamount
                if amount>=200:
                    totalamount = amount
                else:
                    totalamount = amount + shipping
                    fix = 200 - amount
            totalitem = len(cart.objects.filter(user=request.user))
            return render(request, 'app/addtocart.html', {'carts':Cart, 'totalamount':totalamount, 'amount':amount, 'shipping':shipping, 'wshiping':wshiping, 'fix':fix, 'totalitem':totalitem})
        else:
            totalitem = len(cart.objects.filter(user=request.user))
            return render(request, 'app/emptycart.html',{'totalitem':totalitem})
    else:
        return redirect('/accounts/login')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping = 50.0
        wshiping = 0.0
        totalamount = 0.0
        fix = 0.0
        cart_product = [p for p in cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.disc_price)
            amount += tempamount
            if amount>=200:
                totalamount = amount
            else:
                totalamount = amount + shipping
        
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))    
        data = {
            'quantity': c.quantity,
            'totalamount':totalamount,
            'amount':amount,
            'shipping':shipping,
             'wshiping':wshiping,
             'fix':200 - amount,
              'totalitem':totalitem
                }
      
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping = 50.0
        wshiping = 0.0
        totalamount = 0.0
        fix = 0.0
        cart_product = [p for p in cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.disc_price)
            amount += tempamount
            if amount>=200:
                totalamount = amount
            else:
                totalamount = amount + shipping

        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))      
        data = {
            'quantity': c.quantity,
            'totalamount':totalamount,
            'amount':amount,
            'shipping':shipping,
             'wshiping':wshiping,
             'fix':200 - amount,
              'totalitem':totalitem
             
                }
       
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping = 50.0
        wshiping = 0.0
        totalamount = 0.0
        fix = 0.0
        cart_product = [p for p in cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.disc_price)
            amount += tempamount
            if amount>=200:
                totalamount = amount
            else:
                totalamount = amount + shipping

        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))      
        data = {
            'totalamount':totalamount,
            'amount':amount,
            'shipping':shipping,
             'wshiping':wshiping,
             'fix':200 - amount,
              'totalitem':totalitem
             
                }
       
        return JsonResponse(data)
       


@login_required
def buy_now(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/buynow.html',{ 'totalitem':totalitem})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-dark', 'totalitem':totalitem})  
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            locality = form.cleaned_data['locality']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            regs = Customer(user=usr,name=name, number=number, locality=locality, state=state, city=city,zipcode=zipcode)
            regs.save()
            messages.success(request, 'Profile is sucessfully updated')
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-dark', 'totalitem':totalitem})
            
            

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/address.html', {'add':add,'active':'btn-dark', 'totalitem':totalitem})

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    op = op[::-1]
    paginator = Paginator(op,6,orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/orders.html',{'order_placed':op, 'totalitem':totalitem,'order_placed':page_obj})





#def login(request):
 #return render(request, 'app/login.html')

#def customerregistration(request):
 #return render(request, 'app/customerregistration.html')

class URFView(View):
    def get(self, request):
        form = URF()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/URF.html', {'form':form, 'totalitem':totalitem})

    def post(self, request):
        form = URF(request.POST)
        if form.is_valid():
            messages.success(request, 'Welcome to Food Box')
            form.save()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/URF.html', {'form':form, 'totalitem':totalitem})


@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = cart.objects.filter(user=user)
    amount = 0.0
    shipping = 50.0
    wshiping = 0.0
    totalamount = 0.0
    fix = 0.0
    cart_product = [p for p in cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.disc_price)
            amount += tempamount
            if amount>=200:
                totalamount = amount
            else:
                totalamount = amount + shipping
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount, 'amount':amount, 'shipping':shipping, 'wshiping':wshiping, 'fix':fix, 'cart_items':cart_items, 'totalitem':totalitem})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    Cart= cart.objects.filter(user=user)
    for c in Cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return redirect("orders") 




def search(request):
    query = request.POST.get('query', False)    
    title = Product.objects.filter(title__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/food.html', {'title':title,'totalitem':totalitem})


def zsearch(request):
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zfood.html', {'zipcode':zipcode,'totalitem':totalitem})

def zrestro(request):
        query = request.POST.get('query', False)    
        zipcode = Restaurant.objects.filter(zipcode__icontains=query)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(cart.objects.filter(user=request.user))
        return render(request, 'app/zrestro.html',{'zipcode':zipcode, 'totalitem':totalitem})




def ZFineView(request):
    Fine_Dining = Product.objects.filter(category='Fine Dining')
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zfine.html',{'zipcode':zipcode,'Fine_Dining':Fine_Dining, 'totalitem':totalitem})


def ZCasualView(request):
    Casual_Dining = Product.objects.filter(category='Casual Dining')
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zcasual.html',{'zipcode':zipcode,'Casual_Dining':Casual_Dining, 'totalitem':totalitem})


def ZContView(request):
    Contemporary_Casual = Product.objects.filter(category='Contemporary Casual')
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zcont.html',{'zipcode':zipcode,'Contemporary_Casual':Contemporary_Casual, 'totalitem':totalitem})


def ZFamilyView(request):
    Family_Style = Product.objects.filter(category='Family Style')
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zfamily.html',{'zipcode':zipcode,'Family_Style':Family_Style, 'totalitem':totalitem})


def ZFastView(request):
    Fast_Casual = Product.objects.filter(category='Fast Casual')
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zfast.html',{'zipcode':zipcode,'Fast_Casual':Fast_Casual, 'totalitem':totalitem})


def ZFastfoodView(request):
    Fast_Food = Product.objects.filter(category='Fast Food')
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zfastfood.html',{'zipcode':zipcode,'Fast_Food':Fast_Food, 'totalitem':totalitem})


def ZCafeView(request):
    Cafe = Product.objects.filter(category='Cafe')
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zcafe.html',{'zipcode':zipcode,'Cafe':Cafe, 'totalitem':totalitem})


def ZBuffetView(request):
    Buffet = Product.objects.filter(category='Buffet')
    totalitem = 0
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zbuffet.html',{'zipcode':zipcode,'Buffet':Buffet, 'totalitem':totalitem})


def ZTrucksView(request):
    Food_Trucks_and_Concession_Stands = Product.objects.filter(category='Food Trucks and Concession Stands')
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/ztruck.html',{'zipcode':zipcode,'Food_Trucks_and_Concession_Stands':Food_Trucks_and_Concession_Stands, 'totalitem':totalitem})


def ZPopView(request):
    Pop_Up_Restaurant = Product.objects.filter(category='Pop-Up Restaurant')
    query = request.POST.get('query', False)    
    zipcode = Product.objects.filter(zipcode__icontains=query)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(cart.objects.filter(user=request.user))
    return render(request, 'app/zpop.html',{'zipcode':zipcode,'Pop_Up_Restaurant':Pop_Up_Restaurant, 'totalitem':totalitem})

