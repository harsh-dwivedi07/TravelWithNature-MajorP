from dataclasses import fields
from django.http import request
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from places.models import placing,Comment
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm
# Create your views here.
def places(request):
    place=placing.objects.all()
    paginator=Paginator(place,3)
    pagen=request.GET.get('page')
    paged_cars=paginator.get_page(pagen)
    return render(request,'pages/places.html',{'place':paged_cars})

def destination(request,id):
    single_page= get_object_or_404(placing, pk=id)
    #print(placing.comments.all)
    data={
        'single_page':single_page,
        
    }
    return render(request,'pages/destination.html',data)

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name='pages/add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.cur_id=self.kwargs['id']
        form.instance.name=self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('home')
