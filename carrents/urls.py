from.import views
from django.urls import path

urlpatterns=[
   
    path('home/', views.home, name='home'),
    path('rent/<str:id>/', views.rent, name='rent'),
    path('form/<str:id>/', views.fri, name='form'),
    path('register/<str:id>/', views.reg, name='register'),
    path('payments/<str:id>/', views.payments, name='payments'),
    path('flow_payment/<str:ref>/', views.flow_payment, name='flow_payment'),
    path('takes/', views.takes, name='takes')
    
] 