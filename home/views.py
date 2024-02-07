from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        email=request.POST.get('email')
        phoneNo=request.POST.get('phoneNo')
        message=request.POST.get('message')
        contact=Contact(firstName=firstName, lastName=lastName,email=email,phoneNo=phoneNo,message=message)
        contact.save()
        def __str__(self):
            return self.firstName

    return render(request,'contact.html ')