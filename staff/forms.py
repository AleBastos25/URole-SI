from django import forms
from .models import *


# create a ModelForm
class roleForm(forms.ModelForm):
    # # category = forms.MultipleChoiceField(
    # #     choices=Category.CATEGORIAS,
    # #     widget=forms.CheckboxSelectMultiple,
    # #     label='Categoria'
    # # )
    banner_url = forms.URLField(label='URL do banner')
    class Meta:
        model = Role
        fields = ('name', 'role_date', 'role_start_time', 'role_end_time', 'location', 'address', 'banner_url', 'about')
        labels = {
            'name':'Nome do rolê',
            'role_date':'Data',
            'role_start_time':'Horário de Início',
            'role_end_time':'Horário do Fim',
            'location':'Lugar',
            'address':'Endereço',
            'banner_url':'URL do banner do evento',
            'about':'Descrição e Informações'
        }
        widgets = {
                'role_date': forms.DateInput(attrs={'type': 'date'}),
                'role_start_time':forms.TimeInput(attrs={'type': 'time'}),
                'role_end_time':forms.TimeInput(attrs={'type': 'time'}),
            }
    print(Category.CATEGORIAS)    

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