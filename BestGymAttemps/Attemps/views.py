from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def add_attemp(request):
    return render(request, 'add_attemp.html')
