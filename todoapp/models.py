from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64)


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tags")
