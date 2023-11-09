from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('category/<str:id>/', views.category, name='category'),
    path('product/<str:id>/', views.product, name='product'),
    path('products/', views.products, name='products'),
    path('search/', views.search, name='search'),
    path('more/<str:id>/', views.more, name='more'),
    path('addtocart/<str:id>/', views.add_to_cart, name='addtocart'),
    # path('addtowish/<str:id>/', views.add_to_wish, name='addtowish'),
    path('mycart/', views.mycart, name='mycart'),
    # path('wish/', views.wish, name='wish'),
    path('managecart/<str:id>/', views.managecart, name='managecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/<str:id>/', views.payment, name='payment'),
    path('verify_payments/<str:ref>/', views.verify_payments, name='verify_payments'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about')
#   path('update_item/', views.updateItem, name='update_item')
 ]
 