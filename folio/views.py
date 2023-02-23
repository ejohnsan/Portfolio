from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Lista

# Create your views here.

def portfolio(request):

    datos = Lista.objects.all()
    dicc = {"datos":datos}
    plantillas = loader.get_template("folio/portfolio.html")
    documento = plantillas.render(dicc)
    return HttpResponse(documento)

