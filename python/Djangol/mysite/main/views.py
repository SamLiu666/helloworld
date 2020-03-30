from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

# def index(response, id):
#
#     ls = ToDoList.objects.get(id=id)
#     return HttpResponse("<h1> %s  </h1>" % ls.name)

# def index(response, name):
#       # first part
#     ls = ToDoList.objects.get(name=name)
#     item = ls.item_set.get(id=1)
#     return HttpResponse("<h1>%s</h1><br><p>%s</p></br>" % (ls.name, str(item.text)))


def index(response, id):

    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})


def home(response):
    return render(response, "main/home.html", {})

