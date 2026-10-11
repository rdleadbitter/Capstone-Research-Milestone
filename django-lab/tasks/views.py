from django.db.models import Q
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = Task.objects.all()
        query = self.request.GET.get("q", "").strip()
        status = self.request.GET.get("status", "")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(county__icontains=query)
                | Q(defect_type__icontains=query)
                | Q(case_number__icontains=query)
            )

        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by("status", "-score", "-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["statuses"] = Task.STATUS_CHOICES
        context["active_status"] = self.request.GET.get("status", "")
        context["query"] = self.request.GET.get("q", "")
        context["lead_count"] = Task.objects.count()
        context["high_priority_count"] = Task.objects.filter(score__gte=80).count()
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = "/"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = "/"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = "/"