from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from mmain.models import Testimonial,TopPlace
# Create your views here.

def home(request):
    testim=Testimonial.objects.all()
    place=TopPlace.objects.all()
    return render(request,'pages/home.html',{'testim':testim,'place':place})