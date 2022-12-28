from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q


# Create your views here.
def index(request):
    
    return render(request,'index.html',{
        
        'mensaje': 'Proyecto Web con DJango (Desde el View)'
    })

def cursos(request):
    
    return render(request,'index.html',{
        'titulo': 'Listado de cursos'
    })

def crearcursos(request):
    
    return render(request,'index.html',{
        'titulo': 'Agregar cursos'
    })

def carrera(request):
    
    return render(request,'index.html',{
        'titulo': 'Listado de carrreras'
    })

def crearcarrera(request):
   
    return render(request,'index.html',{
        'titulo': 'Agregar carreras'
    })