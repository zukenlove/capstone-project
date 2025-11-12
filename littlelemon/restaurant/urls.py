from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homeView, name='home'),
    path('restaurant/',views.index, name="index"),
    path('menu/',views.menuView, name ='menu'),
]