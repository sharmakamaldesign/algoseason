from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def pricing(request):
    return render(request, 'home/pricing.html')

def contact_us(request):
    return render(request, 'home/contact_us.html')