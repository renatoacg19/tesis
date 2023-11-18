from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.home.forms import *
from core.home.models import Egresos


class EgresosListView(ListView):
    model = Egresos
    template_name = 'egresos/list.html'

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
                for i in Egresos.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de egresos'
        context['create_url'] = reverse_lazy('home:egresos_create')
        context['list_url'] = reverse_lazy('home:egresos_list')
        context['entity'] = 'Egresos'
        return context


class EgresosCreateView(CreateView):
    model = Egresos
    form_class = EgresosForm
    template_name = 'egresos/create.html'
    success_url = reverse_lazy('home:egresos_list')

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
        context['title'] = 'Creación de un egreso'
        context['entity'] = 'Egresos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class EgresosUpdateView(UpdateView):
    model = Egresos
    form_class = EgresosFormEdit
    template_name = 'egresos/create.html'
    success_url = reverse_lazy('home:egresos_list')

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
        context['title'] = 'Edición de un egreso'
        context['entity'] = 'Egresos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class EgresosDeleteView(DeleteView):
    model = Egresos
    template_name = 'egresos/delete.html'
    success_url = reverse_lazy('home:egresos_list')

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
        context['title'] = 'Eliminación de un egreso'
        context['entity'] = 'Egresos'
        context['list_url'] = self.success_url
        return context




