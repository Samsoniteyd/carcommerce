from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('category/<str:id>/', views.category, name='category'),
    path('product/<str:id>/', views.product, name='product'),
    path('brand/', views.brands, name='brand'),
    path('search/', views.search, name='search'),
    path('more/<str:id>/', views.more, name='more'),
    path('addtocart/<str:id>/', views.add_to_cart, name='addtocart'),
    path('mycart/', views.mycart, name='mycart'),
    path('managecart/<str:id>/', views.managecart, name='managecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/<str:id>/', views.payment, name='payment'),
    path('<str:ref>/', views.verify_payment, name='verify-payment'),
#     path('update_item/', views.updateItem, name='update_item')
 ]
