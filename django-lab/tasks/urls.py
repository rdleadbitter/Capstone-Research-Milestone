from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("new/", views.TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/edit/", views.TaskUpdateView.as_view(), name="task-edit"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete")
]