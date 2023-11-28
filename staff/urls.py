from . import views
from django.urls import path

urlpatterns = [
    # CRU Rolês
    path('', views.roles, name='roles'),
    path('create_role', views.RoleCreate.as_view(), name='Criar rolê'),
    path('update_role/<pk>', views.RoleUpdate.as_view(), name='Atualizar rolê'),
    # CRUD Ingressos
    path('tickets/<pk>', views.tickets, name='tickets'),
    path('create_ticket/<pk>', views.TicketCreate.as_view(), name='ticket-create'),
    path('update_ticket/<pk>', views.TicketUpdate.as_view(), name='ticket-update'),
    path('delete_ticket/<pk>', views.TicketDelete.as_view(), name='ticket-delete'),
]