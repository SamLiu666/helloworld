from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response, id):
    return HttpResponse("<h1> Sam Liu  </h1>" % id)

