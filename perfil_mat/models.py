from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

#TABLA MATERIA
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=5, unique=True)
    departamento = models.CharField(max_length=100)
    campus = models.CharField(max_length=100)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nombre
    def get_absolute_url(self): #Redirecciona a la materia agregada
        return reverse('materia_detail', args=[str(self.id)])

#TABLA COMENTARIOS
class Comentario(models.Model):
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name='comentario',
    )
    comentario = models.CharField(max_length=250)      #Comentario
    fecha = models.DateTimeField(auto_now_add=True)  #Fecha del comentario
    autor = models.ForeignKey(                         #Autor del comentario
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.comentario
        
    def get_absolute_url(self):
        return reverse('materia_detail')