from django.shortcuts import render,redirect

# Create your views here.
def places(request):
    return render(request,'pages/places.html')

def destination(request):
    return render(request,'pages/destination.html')
