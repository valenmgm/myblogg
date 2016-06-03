from __future__ import unicode_literals
import datetime

from django.db import models

#importar usuarios
from django.contrib.auth.models import User

# Create your models here.
#class Categoria(models.Model):

#    categoria = models.

class Post(models.Model):

    #Attributes
    titulo = models.CharField(max_length= 120, blank=False)
    fecha = models.DateTimeField(auto_now_add=True, name='fechal')
    contenido = models.TextField(blank=False)
    imagen = models.ImageField(upload_to='post-images', blank=True)

    #Relations
    autor = models.ForeignKey(User, related_name="usuarios_post")

    def make(self, titulo, contenido, imagen, autor):
        self.titulo = titulo
        self.contenido = contenido
        self.imagen = imagen
        self.autor = autor
        return(self)

    def __str__(self):
        return unicode(self.titulo)


class Comment(models.Model):

    #Attributes
    comentario = models.TextField(blank = False)
    fechacomment = models.DateTimeField(auto_now_add=True)

    #Relations
    autorcomment = models.ForeignKey(User, related_name="usuarios_comment")
    posteado = models.ForeignKey(Post, related_name="posteado_a", blank=False, null=False)

    def make(self, comentario, autorcomment, posteado):
        self.comentario = comentario
        self.autorcomment = autorcomment
        self.posteado = posteado
        return(self)

    def __str__(self):
        return unicode(self.autorcomment)
