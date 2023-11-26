# Create your views here.
from accounts.models import Account
from accounts.views import staff_required
from django.contrib.auth.decorators import (login_required,
                                            permission_required,
                                            user_passes_test)
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import roleForm, ticketForm
from .models import Role, Ticket



def base(request):
    return render(request,"base.html")



# Rolês views

class RoleCreate(CreateView):
    template_name = "role/create.html"
    model = Role
    fields = ['name', 'role_date', 'role_start_time', 'role_end_time', 'location', 'address', 'banner_url', 'category', 'about']
    success_url = reverse_lazy('roles')


class RoleUpdate(UpdateView):
    template_name = "role/edit.html"
    model = Role
    fields = ['banner_url', 'category', 'about']
    success_url = reverse_lazy('roles')


class RoleDelete(DeleteView):
    template_name = "role/delete.html"
    model = Role
    success_url = reverse_lazy('roles')

class TicketCreate(CreateView):
    template_name = "ticket/create.html"
    form_class: ticketForm
    model = Ticket
    fields = ['type', 'price']
    success_url = reverse_lazy('tickets')

class TicketUpdate(UpdateView):
    template_name = "ticket/update.html"
    form_class: ticketForm
    model = Ticket
    fields = ['type', 'price']
    success_url = reverse_lazy('tickets')

class TicketDelete(DeleteView):
    template_name = "ticket/delete.html"
    model = Ticket
    success_url = reverse_lazy('tickets')
    

def users(request):
    users = Account.objects.filter(is_staff=False).values_list('username','email', named=True)
    return render(request,"users.html",{'users': users})


######################################## MOVIE VIEWS
@user_passes_test(staff_required, login_url='/accounts/organizerlogin')
def roles(request):
    roles = Role.objects.filter().order_by('-id').values_list('name', 'role_date', 'role_start_time', 'role_end_time', 'location', 'address', 'banner_url', 'category', 'about', named=True)
    return render(request,"roles.html",{'Role_list': roles})

######################################## MOVIE VIEWS
@user_passes_test(staff_required, login_url='/accounts/organizerlogin')
def banners(request):
    banner_data = banner.objects.all().select_related().values_list('id','movie__movie_name','url','modified', named=True)
    return render(request,"banners.html",context = {'banners': banner_data})

############################################## SHOW VIEWS

@user_passes_test(staff_required, login_url='/accounts/organizerlogin')
def shows(request):
    shows = show.objects.all().order_by('-id')
    return render(request,"shows.html",context={'shows':shows})

@user_passes_test(staff_required, login_url='/accounts/organizerlogin')
def users(request):
    users=Account.objects.filter(is_staff=False).all()
    return render(request,"users.html",context={'users':users})

