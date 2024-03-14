
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Moje_wz(models.Model):
    name = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    def __str__(self):
        return self.name

    def learn_url(self):
        return reverse("wz-learn", args=[self.slug])