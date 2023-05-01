from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("teacher/", views.add_teacher, name="add_teacher"),
    path("teachers/", views.teacher_list, name="teachers_display"),
    path("group/", views.add_group, name="add_group"),
    path("groups/", views.group_list, name="group_display"),

]
