from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(null=True, blank=True)
    head_of_department = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    employees = models.ManyToManyField(User, related_name="departments", blank=True)

    def __str__(self) -> str:
        return self.name
