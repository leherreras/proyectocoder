from dataclasses import field
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Curso

# Create your views here.

class CursoList(ListView):

    model = Curso
    template_name = "AppCoder/cursos_list.html"



class CursoDetalle(DetailView):

    model = Curso
    template_name = "AppCoder/curso_detalle.html"


class CursoCreacion(CreateView):

    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']


class CursoDelete(DeleteView):

    model = Curso
    success_url = "/AppCoder/curso/list"


