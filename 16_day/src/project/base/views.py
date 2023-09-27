from django.shortcuts import render
from django.http import HttpResponse

def lista_pendientes(pedido):
    return HttpResponse("Lista de Pendientes")
