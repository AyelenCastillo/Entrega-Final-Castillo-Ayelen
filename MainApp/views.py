from django.http import HttpResponse
from django.shortcuts import render
from .models import Postres, Comidas, Registro
from .forms import miRegistro

def inicio(req):
    return render(req, "inicio.html", {})

def postres(req):
    if req.method == 'POST':
        nueva_comida = Postres(titulo=req.POST['titulo'], receta=req.POST['receta'], autor=req.POST['autor'])
        nueva_comida.save()
        return render(req, "postres.html", {})
    else:
        return render(req, "postres.html", {})

def comidas(req):
    if req.method == 'POST':
        nueva_comida = Comidas(titulo=req.POST['titulo'], receta=req.POST['receta'], autor=req.POST['autor'])
        nueva_comida.save()
        return render(req, "comidas.html", {})
    else:
        return render(req, "comidas.html", {})

def registro(req):
    if req.method == 'POST':
        miFormulario = miRegistro(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nueva_comida = Registro(nombre=data['nombre'], password=data['password'], email=data['email'])
            nueva_comida.save()
            return render(req, "inicio.html", {"message": "Registro Exitoso"})
        else:
            return render(req, "registro.html", {"message": "Registro Invalido"})
    else:
        miFormulario = miRegistro()
        return render(req, "registro.html", {"miFormulario": miFormulario})

def busqueda(req):
    return render(req, "busqueda.html")

def buscar(req):
    titulo = req.GET.get('titulo')
    if titulo:
        resultados_postres = Postres.objects.filter(titulo__icontains=titulo)
        resultados_comidas = Comidas.objects.filter(titulo__icontains=titulo)
        resultados = list(resultados_postres) + list(resultados_comidas)
        if resultados:
            return render(req, "inicio.html", {"results": resultados})
        else:
            return render(req, "inicio.html", {"message": "No se encontraron resultados"})
    else:
        return render(req, "inicio.html", {"message": "Por favor, ingrese un término de búsqueda"})
