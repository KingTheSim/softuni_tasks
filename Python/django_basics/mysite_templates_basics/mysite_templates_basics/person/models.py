from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    height = models.FloatField()
    birth_date = models.DateField()
    wake_up_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_student = models.BooleanField(default=False)
    email = models.EmailField()
    website_url = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="images/", blank=True, null=True)
    document_file = models.FileField(upload_to="files/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.full_name}:\n{self.bio}"
