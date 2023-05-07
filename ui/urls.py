from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('client_service/', views.client_service, name='client_service'),
    path('thanks/', views.thanks, name='thanks'),
]
