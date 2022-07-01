from django.db import models

# Create your models here.


class Link(models.Model):
    target_url = models.URLField(max_length= 200)
    description = models.CharField(max_length= 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
