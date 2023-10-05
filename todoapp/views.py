from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todoapp.forms import TaskCreateForm, TagCreateForm
from todoapp.models import Task, Tag


def index(request: HttpRequest) -> render:
    tasks_list = Task.objects.all()
    context = {"tasks_list": tasks_list}
    if request.method == "POST":
        task_id = request.POST["update_task"]
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()

    return render(request, "todoapp/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todoapp:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todoapp:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todoapp:index")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("todoapp:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todoapp:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todoapp:tag-list")
