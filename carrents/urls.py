from.import views
from django.urls import path

urlpatterns=[
   
    path('home/', views.home, name='home'),
    path('rent/<str:id>/', views.rent, name='rent'),
    path('form/<str:id>/', views.fri, name='form'),
    path('register/<str:id>/', views.reg, name='register'),
    path('payments/<str:id>/', views.payments, name='payments'),
    path('verify-payment/<str:ref>/', views.verify_payment, name='verify-payment'),
    path('booking_list/', views.booking_list, name='booking_list')
    
] 