from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index, name='index'),
    path('about/',views.About, name='about'),
    path('contact/',views.Contact, name='contact'),
    path('shop/',views.Shop, name='shop'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('reg_done/',views.reg_done, name='reg_done'),
]
