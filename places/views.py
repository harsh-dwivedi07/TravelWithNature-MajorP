from django.shortcuts import render,get_object_or_404
from places.models import placing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def places(request):
    place=placing.objects.all()
    paginator=Paginator(place,1)
    pagen=request.GET.get('page')
    paged_cars=paginator.get_page(pagen)
    return render(request,'pages/places.html',{'place':paged_cars})

def destination(request,id):
    single_page= get_object_or_404(placing, pk=id)
    data={
        'single_page':single_page
    }
    return render(request,'pages/destination.html',data)
