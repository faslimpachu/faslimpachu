
from django.urls import path
from . import views

urlpatterns = [
    
    path('hello/',views.hello,name='hello'),
    path('',views.index,name='index'),
    path('contact/', views.contact, name='contact'),
]