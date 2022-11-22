from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
# Create your views here.

def familiares(request):
    
    familiar1=Familiares(nombre="federico",dni=37682175 ,fecha_nacimiento=15/4/1993)
    familiar1.save()
    cadena_texto="familiar 1: "+ familiar1.nombre +" "+ str(familiar1.dni)
    return HttpResponse(cadena_texto)