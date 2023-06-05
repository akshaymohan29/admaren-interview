from django.db import models
from authentication.models import User
# Create your models here.

class Tags(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

class Text_Snippet(models.Model):
    
    title = models.CharField(max_length=255,null=False)
    text = models.TextField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User , on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    
