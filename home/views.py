from django.shortcuts import render, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def loginUser(request):
    # return render(request,'login.html')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        #Check if user has entered correct credentials
        user=authenticate(username=username, password=password)
        if user is not None:
            print("request")  
            #A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            #No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')    

def logoutUser(request):
    logout(request)
    return redirect("/login")

def contact(request):
    if request.method=="POST":
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        email=request.POST.get('email')
        phoneNo=request.POST.get('phoneNo')
        message=request.POST.get('message')
        contact=Contact(firstName=firstName, lastName=lastName,email=email,phoneNo=phoneNo,message=message)
        contact.save()
        messages.success(request, 'Your message has been sent !')

    return render(request,'contact.html ')

