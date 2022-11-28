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
    
    datos= (familiar1.nombre)  + str ( familiar1.dni ) + str ( familiar1.fecha_nacimiento )
    datos2=(familiar2.nombre)  +str(familiar2.dni) + str(familiar3.fecha_nacimiento)
    datos3=(familiar3.nombre) +str (familiar3.dni) + str(familiar3.fecha_nacimiento)

    datos_totales=f"{datos} -- segundo familiar=  {datos2} -- terecer familiar=  {datos3}"
     
    return HttpResponse(datos_totales)  

