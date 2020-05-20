from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView, TemplateView, UpdateView, DeleteView,
)
from django.urls import reverse_lazy
from .forms import PersonaForm

# models
from .models import Empleado


class StartView(TemplateView):
    """ Homepage """
    template_name = 'index.html'


# Create Views
class CreateEmployee(CreateView):
    model = Empleado
    template_name = "persona/create.html"
    form_class = PersonaForm
    success_url = reverse_lazy('persona_app:all')

    def form_valid(self, form):
        # logic
        empleado = form.save()
        fullname = empleado.first_name + ' ' + empleado.last_name
        print('Bienvenido' + ' ' + fullname)
        return super(CreateEmployee,self).form_valid(form)


# Success View
class SuccessView(TemplateView):
    template_name = "persona/success.html"


# Update View
class UpdateEmployee(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:administrador')


# Delete View
class DeleteEmployee(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:administrador')


# Detail Views
class DetailEmpleado(DetailView):
    model = Empleado
    template_name = 'persona/detalle.html'

    def get_context_data(self, **kwargs):
        context = super(DetailEmpleado, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes '
        return context


# List Views
class ListAllEmpleados(ListView):
    """ List all of employees"""
    template_name = 'persona/list_all.html'
    context_object_name = 'empleados'
    ordering = 'first_name'
    paginate_by = 5

    def get_queryset(self):
        key_word = self.request.GET.get("name", '')
        _list = Empleado.objects.filter(
            first_name__icontains=key_word
        )
        return _list


class AdminEmpleados(ListView):
    """ List all of employees"""
    template_name = 'persona/admin_empleados.html'
    context_object_name = 'empleados'
    ordering = 'first_name'
    paginate_by = 10
    model = Empleado


class ListByArea(ListView):
    """List of employees by area or department """
    template_name = 'persona/list_by.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        depart = self.kwargs['depart']
        _list = Empleado.objects.filter(
            department=depart
        )
        return _list


class GetList(ListView):
    """ Using a Textbox """
    template_name = 'persona/byget.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        key_word = self.request.GET.get("name")
        _list = Empleado.objects.filter(
            first_name=key_word
        )
        return _list
