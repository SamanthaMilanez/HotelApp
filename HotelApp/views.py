from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_index(request):
    return render(request,'index.html')

def my_gallery(request):
    return render(request,'gallery.html')

def my_about(request):
    return render(request,'about.html')

def my_booking(request):
    return render(request,'booking.html')


