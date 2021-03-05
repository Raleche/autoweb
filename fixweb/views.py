from django.shortcuts import render
from fixweb.models import Contact

# Create your views here.
def index(request):
    return render(request,"fixweb/index.html")

def about(request):
    return render(request,"fixweb/about.html")

def products(request):
    return render(request,"fixweb/products.html")

def contact(request):
    if request.method == "POST":

        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        ins = Contact(first=first, last=last, email=email, phone=phone, message=message)
        ins.save()

        print("Successfully saved to the DB.")

    return render(request,"fixweb/contact.html")