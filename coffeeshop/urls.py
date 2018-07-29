from django.urls import path
from . import views

urlpatterns = [

    path('', views.providers_list, name='providers_list'),
    path('provider/<int:pk>/', views.provider_detail, name='provider_detail'),
    path('offers/', views.offer_list, name='offer_list'),
    path('provider/new/', views.provider_new, name='provider_new'),
]
