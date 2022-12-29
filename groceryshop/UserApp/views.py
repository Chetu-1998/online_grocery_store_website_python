from django.shortcuts import render,redirect
from AdminApp.models import Category,Product,UserInfo,PaymentMaster
from UserApp.models import MyCart,OrderMaster
from datetime import datetime
from django.contrib import messages

# Create your views here.
def homepage(request):
    cats = Category.objects.all()
    groceries = Product.objects.all()
    return render(request,"homepage.html",{"cats":cats,"groceries":groceries,})

def login(request):
    if (request.method == "GET"):
        return render(request,"login.html",{})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        try:
            user = UserInfo.objects.get(uname=uname,password=password)
            #return redirect(homepage)
        except:
            messages.success(request, 'Invalid Login')
            return redirect(login)
        else:
            request.session["uname"]=uname
            messages.success(request,'Login Successful')
            return redirect(homepage)



def Signup(request):
    if(request.method == "GET"):
        return render(request,"signup.html",{})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = UserInfo(uname,password,email)
        user.save()
        return redirect(homepage)

def Signout(request):
    request.session.clear()
    return redirect(homepage)

def ShowGroceries(request,id):    
    id = Category.objects.get(id=id)   
    groceries = Product.objects.filter(cat = id)
    cats = Category.objects.all()    
    return render(request,"homepage.html",{"cats":cats,"groceries":groceries})

def ViewDetails(request,id):
    grocery = Product.objects.get(id=id)
    return render(request,"ViewDetails.html",{"grocery":grocery})

def addToCart(request):
    if (request.method == "POST"):
        if ("uname" in request.session):
            groceryid = request.POST["groceryid"]
            user = request.session["uname"]
            qty = request.POST["qty"]
            grocery = Product.objects.get(id=groceryid)
            user = UserInfo.objects.get(uname=user)
            try:
                cart = MyCart.objects.get(grocery=grocery,user=user)
            except:
                cart = MyCart()
                cart.user = user
                cart.grocery = grocery
                cart.qty = qty
                cart.save()
            else:
                pass
            return redirect(homepage)
        else:
            return redirect(login)

def ShowAllCartItems(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname=uname)

    if(request.method == "GET"):       
        cartitems = MyCart.objects.filter(user=user)
        total = 0
        for item in cartitems:
            total += item.qty*item.grocery.price
        request.session["total"] = total
        return render(request,"ShowAllCartItems.html",{"items":cartitems})
    else:
        id = request.POST["groceryid"]
        grocery = Product.objects.get(id=id)
        item = MyCart.objects.get(user=user,grocery=grocery)     
        qty = request.POST["qty"]
        item.qty = qty
        item.save()
        return redirect(ShowAllCartItems)   


def removeItem(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    id = request.POST["groceryid"]
    grocery = Product.objects.get(id=id)
    item = MyCart.objects.get(user=user,grocery=grocery)   
    item.delete()
    return redirect(ShowAllCartItems)


def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = PaymentMaster.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(MakePayment)
        else:
            owner = PaymentMaster.objects.get(cardno='111',cvv='111',expiry='02/2025')
            owner.balance += request.session["total"]
            buyer.balance -=request.session["total"]
            owner.save()
            buyer.save()
            uname = request.session["uname"]
            user = UserInfo.objects.get(uname = uname)
            
            order = OrderMaster()
            order.user = user
            order.amount = request.session["total"]
            details = ""
            items = MyCart.objects.filter(user=user)
            for item in items:
                details += (item.grocery.pname)+","
                item.delete()            
            order.details = details
            order.save()
            return redirect(homepage)

def demo(request):
    return render(request,"demo.html",{})

def About(request):
    return render(request,"Aboutus.html",{})

def Contact(request):
    return render(request,"Contact.html",{})

def Termsandcondition(request):
    return render(request,"Termsandcondition.html",{})

def News(request):
    return render(request,"News.html",{})



