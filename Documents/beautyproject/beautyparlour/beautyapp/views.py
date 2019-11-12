from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'beautyapp/home.html')

def about(request):
    return render(request,'beautyapp/aboutus.html')

def services(request):
    return render(request,'beautyapp/services.html')

def spa_treatment(request):
    return render(request,'beautyapp/spa_treatment.html')

def elements(request):
    return render(request,'beautyapp/elements.html')

def contact(request):
    return render(request,'beautyapp/contact.html')
