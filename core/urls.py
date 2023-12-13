from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


# from .views import say_hello

urlpatterns = [
    path("home/", views.index, name="index"),
    path("teachers/", views.teachers, name="teachers"),
    path("", views.say_hello, name="hlw"),
    path("test/", views.test, name="test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
