from django.urls import path
from . import views

urlpatterns = [
    path('usersignin/', views.user_login, name='Login'),
    path('userregister/', views.user_signup, name='Cadastro'),
    path('organizerlogin/', views.organizer_login, name='Login - Organizador'),
    path('logout/', views.signout, name="logout"), 

]