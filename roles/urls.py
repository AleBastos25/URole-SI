from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'), 
    path('detail/<id>', views.role_detail, name="detalhes"), 
    path('ticket_selection/<id>', views.ticket_selection, name="detalhes"), 
]