from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "case_number",
            "county",
            "defect_type",
            "score",
            "status",
            "description",
        ]