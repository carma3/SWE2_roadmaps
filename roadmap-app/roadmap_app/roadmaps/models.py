from django.db import models

# Create your models here.

class ClassGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=25)


    def __str__(self):
        return self.group_name



class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=25)
    group_id = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title


class Roadmap(models.Model):
    roadmap_id = models.AutoField(primary_key=True)
    roadmap_title = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.roadmap_title

class Attachment(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    attachment_roadmap = models.ForeignKey(Roadmap, on_delete=models.DO_NOTHING)
    attachment_name = models.CharField(max_length=75)

    def __str__(self):
        return self.attachment_name