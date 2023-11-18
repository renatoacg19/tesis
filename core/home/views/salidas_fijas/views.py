from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.home.forms import *
from core.home.models import salidas_fijas


class Salidas_fijasListView(ListView):
    model = salidas_fijas
    template_name = 'salidas_fijas/list.html'

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
                for i in salidas_fijas.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de salidas fijas'
        context['create_url'] = reverse_lazy('home:salidas_fijas_create')
        context['list_url'] = reverse_lazy('home:salidas_fijas_list')
        context['entity'] = 'Salidas_fijas'
        return context


class Salidas_fijasCreateView(CreateView):
    model = salidas_fijas
    form_class = Salidas_fijasForm
    template_name = 'salidas_fijas/create.html'
    success_url = reverse_lazy('home:salidas_fijas_list')

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
        context['title'] = 'Creación de una salida fija'
        context['entity'] = 'Salidas fijas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class Salidas_fijasUpdateView(UpdateView):
    model = salidas_fijas
    form_class = Salidas_fijasFormEdit
    template_name = 'salidas_fijas/create.html'
    success_url = reverse_lazy('home:salidas_fijas_list')

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
        context['title'] = 'Edición de una salida fija'
        context['entity'] = 'Productos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class Salidas_fijasDeleteView(DeleteView):
    model = salidas_fijas
    template_name = 'salidas_fijas/delete.html'
    success_url = reverse_lazy('home:salidas_fijas_list')

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
        context['title'] = 'Eliminación de una salida fija'
        context['entity'] = 'Salidas_fijas'
        context['list_url'] = self.success_url
        return context




