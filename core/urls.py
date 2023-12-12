from django.urls import path
from . import views

# from .views import say_hello

urlpatterns = [
    path("home/", views.index, name="index"),
    path("teachers/", views.teachers, name="teachers"),
    path("", views.say_hello, name="hlw"),
    path("test/", views.test, name="test"),
]
