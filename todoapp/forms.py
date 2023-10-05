from asyncio import Task

from django import forms
from django.forms import fields

from todoapp.models import Tag, Task


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = fields.DateField(
        widget=forms.widgets.DateInput(attrs={"type": "date"}), required=False
    )

    class Meta:
        model = Task
        fields = ("content", "tags", "deadline")


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
