from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def service_details(request):
    return render(request,'service_details.html')

def image_gallery(request):
    return render(request,'image_gallery.html')

def blog(request):
    return render(request,'blog.html')

def single_blog(request):
    return render(request,'single_blog.html')

def contact(request):
    return render(request,'contact.html')

