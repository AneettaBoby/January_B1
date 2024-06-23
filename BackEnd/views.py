from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from Webapp.models import Contact_db
from django.contrib import messages

from BackEnd.models import ecommerce_db, product_db


# Create your views here.
def index_page(request):
    return render(request,"index.html")
def categories_page(request):
    return render(request,"AddCategories.html")
def save_categories(request):
    if request.method=="POST":
        name=request.POST.get('na')
        descriptipn= request.POST.get('desc')
        img = request.FILES['image']
        obj = ecommerce_db(Name=name,Desicription=descriptipn, C_image=img)
        obj.save()
        messages.success(request,"Category saved successfully......!")
        return redirect(categories_page)
def display_category(request):
    data=ecommerce_db.objects.all()
    return render(request,"display.html",{'data':data})
def Edit_page(request,e_id):
    data=ecommerce_db.objects.get(id=e_id)
    return render(request,"Edit.html",{'data':data})

def Update_image(request,e_id):
    if request.method == "POST":
        name = request.POST.get('na')
        descriptipn = request.POST.get('desc')
        try:
            img = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=ecommerce_db.objects.get(id=e_id).C_image
        ecommerce_db.objects.filter(id=e_id).update(Name=name,Desicription=descriptipn,C_image=file)
        return redirect(display_category)
def delete_page(request,e_id):
    data=ecommerce_db.objects.filter(id=e_id)
    data.delete()
    messages.error(request,"Deleted....!!!!")
    return redirect(display_category)
def login_page(request):
    return render(request,"Login.html")
def adminLogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"Welcome....")
                return redirect(index_page)
            else:
                messages.error(request,"invalid password.......")
                return redirect(login_page)
        else:
            messages.warning(request,"User not found...!")
            return redirect(login_page)
def Product_page(request):
    cat=ecommerce_db.objects.all()
    return render(request,"products.html",{'cat':cat})
def save_products(request):
    if request.method=="POST":
        product_Na=request.POST.get('P_name')
        name=request.POST.get('pname')
        pr=request.POST.get('price')
        descriptipn= request.POST.get('desc')
        img = request.FILES['pimage']
        obj = product_db(Category=product_Na,P_Name =name,P_price=pr,Desicription=descriptipn,P_image =img)
        obj.save()
        messages.success(request,"products added succeesfully.....!!!!")
        return redirect(Product_page)


def display_product(request):
    data = product_db.objects.all()
    return render(request, "produt_display.html", {'data': data})
def Edit_product(request,pro_id):
    pro= product_db.objects.get(id=pro_id)
    cat=ecommerce_db.objects.all()
    return render(request,"Edit_product.html",{'pro':pro,'cat':cat})
def Update_ProductImage(request,pro_id):
    if request.method == "POST":
        product_Na = request.POST.get('P_name')
        name = request.POST.get('pname')
        pr = request.POST.get('price')
        descriptipn = request.POST.get('desc')
        try:
            img = request.FILES['pimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=product_db.objects.get(id=pro_id).P_image
        product_db.objects.filter(id=pro_id).update(Category=product_Na,P_Name =name,P_price=pr,Desicription=descriptipn,P_image =file)
        return redirect(display_product)
def contact_details(request):
    data=Contact_db.objects.all()
    return render(request,"ContactData.html",{'data':data})