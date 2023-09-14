from django.urls import path, include
from travelapp import views

urlpatterns = [
   path('',views.demo,name='demo'),

]