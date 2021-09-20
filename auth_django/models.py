from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)
    
class Test(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()