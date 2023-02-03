from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Contact

# Create your views here.


class ContactList(ListView):
    model = Contact


class ContactDetails(DetailView):
    model = Contact
    template_name = 'contactapp/contact_details.html'


class CreateContact(CreateView):
    model = Contact
    fields = ['name', 'email', 'address', 'cell']
    success_url = reverse_lazy('contact_list')
    template_name = 'contactapp/contact_form.html'


class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name', 'email', 'address', 'cell']
    success_url = reverse_lazy('contact_list')
    template_name = 'contactapp/contact_form.html'


class ContactDelete(DeleteView):
    model = Contact
    template_name = 'contactapp/contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')


def home(request):
    return render(request, 'index.html')
