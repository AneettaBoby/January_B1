from django.shortcuts import render, redirect
from BackEnd.models import product_db,ecommerce_db
from Webapp.models import Contact_db, Register_db, CartDb, CheckoutDb
from django.contrib import messages
import razorpay


# Create your views here.
def homepage(request):
    cat=ecommerce_db.objects.all()
    return render(request,"home.html",{'category':cat})
def aboutpage(request):
    return render(request,"about.html")
def Contactpage(request):
    cat = ecommerce_db.objects.all()
    return render(request,"contact.html",{'category':cat})
def Productpage(request):
    pro=product_db.objects.all()
    return render(request,"OurProduct.html",{'products':pro})
def save_contact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em= request.POST.get('email')
        ph = request.POST.get('phone')
        sub= request.POST.get('subject')
        msg = request.POST.get('message')
        obj=Contact_db(Name=na,Email=em,Phone=ph,Subject=sub,Message= msg )
        obj.save()
        return redirect(Contactpage)
def filtered_products(request,cat_name):
    data=product_db.objects.filter(Category=cat_name)
    # cat = ecommerce_db.objects.all()
    return render(request,"Filtered_products.html",{'data':data})
def single_page(request,pro_id):
    data=product_db.objects.get(id=pro_id)
    return render(request,"single_product.html",{'data':data})
def register_page(request):
    return render(request,"register.html")
def save_register(request):
    if request.method == "POST":
        name = request.POST.get('na')
        email = request.POST.get('em')
        paswd= request.POST.get('pwd1')
        cofirm_pwd=request.POST.get('pwd2')
        obj=Register_db(Username=name,Email=email,Password=paswd,Confirm_password=cofirm_pwd)
        if Register_db.objects.filter(Username=name).exists():
            messages.warning(request,"Username already exist...!")
            return redirect(register_page)
        elif Register_db.objects.filter(Email=email).exists():
            messages.warning(request, "Email already exist...!")
            return redirect(register_page)
        else:
            obj.save()
            messages.success(request, "Registered successfully...!")
        return redirect(register_page)
def UserLogin(request):
    if request.method=="POST":
        un=request.POST.get("uname")
        pswd=request.POST.get("password")
        if Register_db.objects.filter(Username=un,Password=pswd).exists():
            request.session['username']=un
            request.session['password']=pswd
            messages.success(request, "successfully Login....")
            return redirect(homepage)
        else:
            return redirect(register_page)
    else:
        return redirect(register_page)
def UserLogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "successfully Logout....")
    return redirect(homepage)
def save_cart(request):
    if request.method=="POST":
        username=request.POST.get("u_name")
        P_Name=request.POST.get("p_name")
        qty=request.POST.get("quantity")
        total=request.POST.get("t_price")
        obj=CartDb(Username=username,ProductName=P_Name,Quantity=qty,Totalprice=total)
        obj.save()
        messages.success(request, "successfully added products....")
        return redirect(homepage)
def cart_page(request):
    data=CartDb.objects.filter(Username=request.session['username'])
    subtotal=0
    shipping_charge=0
    total=0
    for d in  data:
        subtotal=subtotal+d.Totalprice
        if subtotal>=500:
            shipping_charge=50
        else:
            shipping_charge=100
        total=subtotal+shipping_charge
    return render(request,"cart.html",{'data_product':data,'subtotal':subtotal,'total':total,'shipping_charge':shipping_charge})
def delete_item(request,P_id):
    x=CartDb.objects.filter(id=P_id)
    x.delete()
    return redirect(cart_page)

def user_login_page(request):
   return render(request,"Userlogin.html")
def checkout_page(request):
    products=CartDb.objects.filter(Username=request.session['username'])
    subtotal = 0
    shipping_charge = 0
    total = 0
    for d in products:
        subtotal = subtotal + d.Totalprice
        if subtotal >= 500:
            shipping_charge = 50
        else:
            shipping_charge = 100
        total = subtotal + shipping_charge
    return render(request,"checkout.html",{'products':products,'subtotal':subtotal,'total':total,'shipping_charge':shipping_charge})
def payment_page(request):

    #Retrive the CheckoutDb object with the specified id
    customer=CheckoutDb.objects.order_by('-id').first()


    #Get the payment amount of the specified customer
    payy=customer.Totalprice

    #convert amount to Paisa(smallest currency unit)
    amount=int(payy*100)


    #convert amount to string for printing
    payy_str=str(amount)


    #printing each character of the payment amount
    for i in payy_str:
        print(i)


    if request.method=="POST":
        order_currency="INR"
        client=razorpay.Client(auth=('rzp_test_TrXkR4gsjBY3MC','oQQRbVSlhL3MlOi0ZveUSrxl'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})
    return render(request,"payment.html",{'customer':customer,'payy_str':payy_str})
def save_checkout(request):
    if request.method=="POST":
        name=request.POST.get("u_name")
        email=request.POST.get("em")
        address = request.POST.get("adrs")
        phone=request.POST.get("mob")
        Price=request.POST.get("total")
        obj=CheckoutDb(Name=name,Email=email,Address=address,Phone=phone,Totalprice=Price)
        obj.save()
        return redirect(payment_page)

