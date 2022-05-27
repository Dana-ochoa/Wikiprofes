from django import forms
from django.forms import fields

from perfil_mat.models import Comentario

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('comentario',)
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
        }