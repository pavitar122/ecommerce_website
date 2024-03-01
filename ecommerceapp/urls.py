from django.urls import path, include
from ecommerceapp import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('copy/', views.copy, name="copy"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")
    
]
