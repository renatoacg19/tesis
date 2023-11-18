from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.home.forms import *
from core.home.models import ingresos


class IngresosListView(ListView):
    model = ingresos
    template_name = 'ingresos/list.html'

    # permission_required = 'view_cartas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in ingresos.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de ingresos'
        context['create_url'] = reverse_lazy('home:ingresos_create')
        context['list_url'] = reverse_lazy('home:ingresos_list')
        context['entity'] = 'ingresos'
        return context


class IngresosCreateView(CreateView):
    model = ingresos
    form_class = IngresosForm
    template_name = 'ingresos/create.html'
    success_url = reverse_lazy('home:ingresos_list')

    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Ingreso'
        context['entity'] = 'Ingresos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class IngresosUpdateView(UpdateView):
    model = ingresos
    form_class = IngresosFormEdit
    template_name = 'ingresos/create.html'
    success_url = reverse_lazy('home:ingresos_list')

    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un ingreso'
        context['entity'] = 'Ingresos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class IngresosDeleteView(DeleteView):
    model = ingresos
    template_name = 'ingresos/delete.html'
    success_url = reverse_lazy('home:ingresos_list')

    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Ingresos'
        context['entity'] = 'Ingresos'
        context['list_url'] = self.success_url
        return context




