from django.urls import path
from .views import (
    MatAllView,
    MatDetailView,
    MatCreateView,
    MatUpdateView,
    MatDeleteView,
    CommentDeleteView,
    CommentCreateView,
    SearchMateriaListView,
    ContactoView,
)

urlpatterns = [
    path('', MatAllView.as_view(), name='materia_all'),  #Aqui se ven todas las materias
    path('materia/<int:pk>/', MatDetailView.as_view(), name='materia_detail'), #Aqui se ve solo una materia
    path('materia/new/', MatCreateView.as_view(), name='materia_new'),   #Para agregar materia
    path('materia/<int:pk>/edit/', MatUpdateView.as_view(), name='materia_edit'),  #Para editar una materia
    path('materia/<int:pk>/delete/', MatDeleteView.as_view(), name='materia_delete'), #Para eliminar materia
    path('contacto/', ContactoView.as_view(), name='contacto'),  #Aqui se ven todas las materias

    #Comentarios
    path('<int:pk>/delete_comment/', CommentDeleteView.as_view(), name='mat_comment_delete'), #Elimina comentario de materia
    path('<int:pk>/new_comment/', CommentCreateView.as_view(), name='mat_comment_new'), #agrega un comentario
    path('search/', SearchMateriaListView.as_view(),name='search_materia'), #Lista de materias a buscar

]