from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    
