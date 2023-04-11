import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.title
