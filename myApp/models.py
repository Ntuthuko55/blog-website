from django.db import models

# Create your models here.
class destination(models.Model):
    Title=models.CharField(max_length=256)
    topic=models.CharField(max_length=256)
    article=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    
class comments(models.Model):
    dests=models.ForeignKey(destination,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body = models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    