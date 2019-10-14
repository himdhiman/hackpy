from django.urls import path

from auth import views

urlpatterns = [
    path('login/', views.Login , name = 'login'),
    path('logout/', views.Logout , name = 'logout'),
    path('createUser/', views.CreateUser, name = 'createuser')
]