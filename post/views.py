from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
#
from . import models
from . import forms
# Create your views here.

def index(request):
    publicacion = models.Post.objects.all()
    return render(request, 'index.html', {'datos': publicacion})

@csrf_exempt
def detail(request, idp):
    infopost = models.Post.objects.get(pk = idp)
    infocomments = models.Comment.objects.filter(posteado__id = idp)#post_id = pk
    form = forms.FormComentario()

    if request.method =='POST':
        formset = forms.FormComentario(request.POST)
        if formset.is_valid():
            data = formset.cleaned_data
            comentario = data['comentario']
            autorcomment = data['autorcomment']
            posteado = infopost

            nuevo = models.Comment()
            nuevo = nuevo.make(comentario, autorcomment, posteado)
            nuevo.save()

    return render(request, 'detail.html', {"datospost":infopost, "datoscomment":infocomments, "formfill":form})


@csrf_exempt
def newpost(request):
    formNP = forms.FormPost()
    if request.method == 'POST':
        formset = forms.FormPost(request.POST)
        if formset.is_valid():
            data = formset.cleaned_data
            titulo = data['titulo']
            contenido = data['contenido']
            imagen = data['imagen']
            autor = data['autor']

            nuevopost = models.Post()
            nuevopost = nuevopost.make(titulo, contenido, imagen, autor)
            nuevopost.save()

            idnew = models.Post.objects.latest('fechal')
            return redirect('detalle', idnew.id)
            #return redirect(detail(args=[request, idnew.id]))

    return(render(request, 'newpost.html', {'formfill':formNP}))
