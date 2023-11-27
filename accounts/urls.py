from django.urls import path
from . import views

urlpatterns = [
    path('usersignin/', views.user_login, name='Login'),
    path('userregister/', views.user_signup, name='Cadastro'),
    path('stafflogin/', views.staff_login, name='Login - Organizador'),
    path('logout/', views.signout, name="logout"), 

]