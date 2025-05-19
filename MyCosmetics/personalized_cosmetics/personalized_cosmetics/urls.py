from django.contrib import admin
from django.urls import path
from cosmetics import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('page1/', views.page1, name='page1'),  
    path('personalize/', views.personalize, name='personalize'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),
    path('tips/', views.tips, name='tips'),
    path('blank/', views.blank, name='blank'),
]