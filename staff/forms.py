from django import forms
from .models import *


# create a ModelForm
class roleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = ('name', 'role_date', 'role_start_time', 'role_end_time', 'location', 'address', 'banner_url', 'category', 'about')
        labels = {
            'name':'Nome do rolê',
            'role_date':'Data',
            'role_start_time':'Horário de Início',
            'role_end_time':'Horário do Fim',
            'location':'Lugar',
            'address':'endereço',
            'banner_url':'URL do banner do evento',
            'category':'Categoria',
            'about':'Descrição e Informações'
        }
        widgets = {
                'date': forms.DateInput(attrs={'type': 'date'}),
                'role_start_time':forms.TimeInput(attrs={'type': 'time'}),
                'role_end_time':forms.TimeInput(attrs={'type': 'time'}),
            }

    def __str__(self):
        return self.name


class ticketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('type', 'price')
        labels = {
            'type':'Nome do ingresso',
            'price':'preço'
        }
    def __str__(self):
        return self.movie_name