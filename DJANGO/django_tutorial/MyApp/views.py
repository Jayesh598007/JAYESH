
from django.shortcuts import render, HttpResponse
from datetime import datetime
from MyApp.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'variable1': "This statement is added through 'variables'",
        'variable2': "Jayesh is great"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Home, Jayesh\n Welcome to django")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse(" Jayesh is a good boy, he is very studious and Hard-Working.\n This is what we know about him")

def service(request):
    return render(request, 'service.html')
    # return HttpResponse(" We are the Leading Business consultant in Pune. Call us on Out Toll-Free-Number : 1800 600 2323")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email= email, phone= phone, desc= desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your request has been successfully send!!")
        
    return render(request, 'contact.html')
    # return HttpResponse(" Contact us on : jayeshchau598007@gmail.com")

    