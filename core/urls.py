from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("todo/", add_to_do, name="todo_add")
]
