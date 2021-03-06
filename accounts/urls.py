from django.urls import path

from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),

    path('', views.home, name='index'),
    path('dashboard', views.home, name='dashboard'),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('products', views.products, name='products'),

    path('create_order/<str:pk>', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('update_customer/<str:pk>', views.updateCustomer, name="update_customer"),

]
