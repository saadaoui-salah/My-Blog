from django.db import models
from user.models import Author


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title  = models.CharField(max_length=100)
    body   = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    