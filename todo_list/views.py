from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from .forms import TaskForm
from .models import Tag, Task


class HomePage(generic.ListView):
    model = Task
    template_name = "todo/home_page.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("catalog:home-page")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("catalog:home-page")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:home-page")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tags_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")


class ToggleAssignToTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)

        task.is_completed = not task.is_completed
        task.save()

        return redirect(reverse_lazy(
            "catalog:home-page"
        ))
