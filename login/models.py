from django.db import models
from django.contrib.auth.models import User


class Ngo(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=266)
