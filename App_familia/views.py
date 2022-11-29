from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import Template , Context 

from django.shortcuts import render
# Create your views here.

def familiares(request):
    

    
    familiar1=Familiares(nombre="federico",dni=37682175 ,fecha_nacimiento="1993-04-15")
    familiar2=Familiares(nombre="marta",dni=6543254 ,fecha_nacimiento="1993-01-10")
    familiar3=Familiares(nombre="gaston",dni=55555555 ,fecha_nacimiento="1996-10-25")
    familiar1.save()
    familiar2.save()
    familiar3.save()


    plantilla=open("C:/Users/fede1/Desktop/mtvfederico/mvtfederico/mvtfederico/plantillas/template.html")
    template= Template(plantilla.read())
    plantilla.close()

    contexto=Context({"persona1": familiar1 , "persona2": familiar2 , "persona3": familiar3})

    documento= template.render(contexto)

    return HttpResponse(documento)
    
    


