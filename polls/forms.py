from django import forms
from .models import Teacher, Group


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "age", "subjects"]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "capacity"]
