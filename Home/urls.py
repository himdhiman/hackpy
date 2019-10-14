from django.urls import path

from Home import views

urlpatterns = [
    path('', views.HomePage.as_view(), name = 'homepage')
]