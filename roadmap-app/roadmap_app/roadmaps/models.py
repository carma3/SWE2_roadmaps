from django.db import models

# Create your models here.

class Roadmap(models.Model):
    roadmap_id = models.AutoField(primary_key=True)
    roadmap_title = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)