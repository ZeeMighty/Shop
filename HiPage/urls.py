
from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from HiPage.models import Good


urlpatterns = [

    url(r'^$', views.IndexView, name = 'index'),
    url(r'men/', view.Men, name = 'men'),

    url(r'aboutus/', views.AboutUs, name = 'aboutus'),
    url(r'terms/', views.Terms, name = 'terms'),
    url(r'delivery/', views.Delivery, name = 'delivery'),
    url(r'return-policy/', views.Refund, name = 'refundpolicy'),
    url(r'support/', views.Support, name = 'support'),

]
