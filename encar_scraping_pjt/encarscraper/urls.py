from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_cars/', views.index, name='search_cars')
]
