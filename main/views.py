from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Welcome to homepage! <strong>#samoOIRI</strong>')
