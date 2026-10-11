from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("review", "Needs review"),
        ("contacted", "Contacted"),
        ("closed", "Closed"),
    ]

    title = models.CharField(max_length=120)
    case_number = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=60, blank=True)
    defect_type = models.CharField(max_length=80, blank=True)
    score = models.PositiveIntegerField(default=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title