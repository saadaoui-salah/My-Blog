from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    username = None
    email    = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email