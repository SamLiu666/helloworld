from django.urls import path
from . import views

# urlpatterns = [
#     path("<int:id>", views.index, name="index"),
# ]

urlpatterns = [
    # path("<str:name>", views.index, name="index"),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),      # 什么都不输入，通过views访问主页
    path("create/", views.create, name="create"),

]