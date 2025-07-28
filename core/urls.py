from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


# from .views import say_hello

urlpatterns = [
    path("", views.home, name="home"),
    path("headmaster_speech/", views.headmaster_speech, name="headmaster_speech"),
    path("teachers/", views.teachers, name="teachers"),
    path("teachers_vocational/", views.teachers_vocational, name="teachers_vocational"),
    path("teacher/<int:pk>/", views.single_teacher, name="single_teacher"),
    path("test/", views.say_hello, name="hlw"),
    path("test2/", views.test, name="test"),
    path("about/", views.about_us, name="about"),
    path("notice/", views.notice, name="notice"),
    path("class_routine/", views.class_routine, name="class_routine"),
    path(
        "management_committee/", views.management_committee, name="management_committee"
    ),
    path("staff_members/", views.staff_members, name="staff_members"),
] 
