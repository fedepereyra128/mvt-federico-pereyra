from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import Template , Context 
# Create your views here.

def familiares(request):
    
    familiar1=Familiares(nombre="federico",dni=37682175 ,fecha_nacimiento="1993-04-15")
    familiar2=Familiares(nombre="marta",dni=6543254 ,fecha_nacimiento="1993-01-10")
    familiar3=Familiares(nombre="gaston",dni=55555555 ,fecha_nacimiento="1996-10-25")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    cadena_texto="familiar 1: "+ familiar1.nombre +" "+ str(familiar1.dni)
    
    
    return render(request,"C:/Users/fede1/Desktop/mtvfederico/mvtfederico/mvtfederico/plantillas/template.html")

def html1(request):
    
    archivo=open("C:/Users/fede1/Desktop/mtvfederico/mvtfederico/mvtfederico/plantillas/template.html")
    template=Template(archivo.read())
    archivo.close()
    contexto=Context()
    documento= template.render(contexto)
    return HttpResponse (documento)

