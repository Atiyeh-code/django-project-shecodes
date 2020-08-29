from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm


class CustomUser(AbstractUser):
    # this is where I would put custom fields

    first_name = models.CharField(max_length=30, verbose_name='first name')
    last_name = models.CharField(max_length=100, verbose_name='last name')

    def __str__(self):
        return self.username


