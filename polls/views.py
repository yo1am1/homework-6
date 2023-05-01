from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TeacherForm, GroupForm
from .models import Teacher, Group


def index(request):
    return render(request, "index.html")


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("teachers_display")

    else:
        form = TeacherForm()
    return render(request, "teacher_add_form.html", {"form": form})


def add_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("group_display")

    else:
        form = GroupForm()
    return render(request, "group_add_form.html", {"form": form})


def teacher_list(request):
    teachers = Teacher.objects.values()
    return render(request, "teachers.html", {"teachers": teachers})


def group_list(request):
    groups = Group.objects.values()
    return render(request, "groups.html", {"groups": groups})
