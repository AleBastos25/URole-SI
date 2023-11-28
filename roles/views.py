
from django.shortcuts import render
from .models import *



def home(request):
    roles = Role.objects.filter().values_list('id','name', 'banner_url', named=True)
    return render(request,"index.html", context={'roles': roles})

def role_detail(request,id):
    context = {}
    context['role'] = Role.objects.get(id = id) 
    return render(request,"role_detail.html",context)

def ticket_selection(request, id):
    tickets = Ticket.objects.filter(role=Role.objects.get(id=id)).values_list('type','price', named=True)
    return render(request,"ticket_selection.html", context={'tickets': tickets})