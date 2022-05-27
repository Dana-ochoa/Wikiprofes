from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin #Autorizacion
from django.urls import reverse_lazy
from .forms import CommentForm
from django.db.models import Q


from .models import Comentario, Materia    #Se importa la tabla Materia

#Todas las materias
class MatAllView(ListView):
    model = Materia
    template_name = 'materia_all.html'

class ContactoView(ListView):
    model = Materia
    template_name = 'contacto.html'

#Para ver materia individual
class MatDetailView(DetailView):
    model = Materia
    template_name = 'materia_detail.html'

#Para agregar nueva materia
class MatCreateView(LoginRequiredMixin, CreateView):
    model = Materia
    template_name = 'materia_new.html'
    fields = ['nombre', 'clave', 'departamento', 'campus'] #Los campos a editar
    login_url = 'login'

    def form_valid(self, form): #permiso
        form.instance.autor = self.request.user
        return super().form_valid(form)

#Para editar una materia
class MatUpdateView(UpdateView):
    model = Materia
    template_name = 'materia_edit.html'
    fields = ['nombre', 'clave', 'departamento', 'campus',] #Los campos a editar
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs): #permiso para editar
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

#Para eliminar una materia
class MatDeleteView(DeleteView):
    model = Materia
    template_name = 'materia_delete.html'
    success_url = reverse_lazy('materia_all')  #redirecciona a materia_all
    login_url = 'login'

#Para agregar un nuevo comentario
class CommentCreateView(LoginRequiredMixin, CreateView):#crea un nuevo comentario
    model = Comentario
    template_name = 'mat_comment_new.html'
    form_class = CommentForm #importamos forms
    success_url = reverse_lazy('materia_all')
    
    def form_valid(self, form):
        form.instance.materia_id = self.kwargs['pk']
        form.instance.autor = self.request.user
        return super ().form_valid(form)

#Para eliminar el comentario de una materia
class CommentDeleteView(DeleteView):
    model = Comentario
    template_name = 'mat_comment_delete.html'
    success_url = reverse_lazy('materia_all')
    login_url = 'login'

class SearchMateriaListView(ListView):
    model = Materia
    context_object_name = 'materia_all'
    template_name = 'search_materia.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Materia.objects.filter(  #Busca por clave y nombre de materia
            Q(clave__icontains = query) | Q(nombre__icontains = query)
        )