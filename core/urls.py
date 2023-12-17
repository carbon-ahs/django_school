from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


# from .views import say_hello

urlpatterns = [
    path("", views.home, name="home"),
    path("teachers/", views.teachers, name="teachers"),
    path("teacher/<int:pk>/", views.single_teacher, name="single_teacher"),
    path("test/", views.say_hello, name="hlw"),
    path("test2/", views.test, name="test"),
    path("about/", views.test, name="about"),
    path("notice/", views.notice, name="notice"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
