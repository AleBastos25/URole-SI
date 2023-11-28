# Create your views here.
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from accounts.models import Account
from accounts.views import staff_required
from django.contrib.auth.decorators import (login_required,
                                            permission_required,
                                            user_passes_test)
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import roleForm, ticketForm
from .models import Role, Ticket



def base(request):
    return render(request,"base.html")


class RoleCreate(CreateView):
    template_name = "role/create.html"
    form_class = roleForm
    model = Role
    success_url = reverse_lazy('roles')


class RoleUpdate(UpdateView):
    template_name = "role/edit.html"
    model = Role
    form_class = roleForm
    success_url = reverse_lazy('roles')


class TicketCreate(CreateView):
    template_name = "ticket/create.html"
    form_class = ticketForm
    model = Ticket
    def get_success_url(self):
        return reverse("tickets", args=[self.kwargs['pk']])
    def form_valid(self, form):
        form.instance.role = Role.objects.filter(id=self.kwargs['pk'])[0]
        return super().form_valid(form)

class TicketUpdate(UpdateView):
    template_name = "ticket/edit.html"
    form_class = ticketForm
    model = Ticket
    def get_success_url(self):
        return reverse("tickets", args=[Ticket.objects.filter(id=self.kwargs['pk'])[0].role.id])

class TicketDelete(DeleteView):
    template_name = "ticket/delete.html"
    model = Ticket
    def get_success_url(self):
        return reverse("tickets", args=[Ticket.objects.filter(id=self.kwargs['pk'])[0].role.id])
    

def users(request):
    users = Account.objects.filter(is_staff=False).values_list('username','email', named=True)
    return render(request,"users.html",{'users': users})


######################################## MOVIE VIEWS
@user_passes_test(staff_required, login_url='/accounts/stafflogin')
def roles(request):
    roles = Role.objects.filter().order_by('-id').values_list('id','name', 'role_date', 'role_start_time', 'role_end_time', 'location', 'address', 'banner_url', 'about', named=True)
    return render(request,"roles.html",{'role_list': roles})

@user_passes_test(staff_required, login_url='/accounts/stafflogin')
def tickets(request, pk):
    tickets = Ticket.objects.all().filter(role__id=pk)
    return render(request,"tickets.html",context={'tickets':tickets, 'role_id':pk})

@user_passes_test(staff_required, login_url='/accounts/stafflogin')
def users(request):
    users=Account.objects.filter(is_staff=False).all()
    return render(request,"users.html",context={'users':users})

