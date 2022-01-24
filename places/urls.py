from django.http import request
from django.urls import path
from django.urls.conf import include
from . import views
from mmain import views as v

urlpatterns = [
    path('', views.places, name='places'),
    path('<int:id>',views.destination,name='destination'),
    #path('/comment',views.aComment,name='aComment'),
     path('<int:id>/comment',views.AddCommentView.as_view(),name='add_comment')
    
]