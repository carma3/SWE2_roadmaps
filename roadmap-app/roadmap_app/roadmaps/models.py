from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=25)
    student_email = models.CharField(max_length=25)
    student_username = models.CharField(max_length=25)
    student_password = models.CharField(max_length=30) # TODO: Hash this
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    instructor_name = models.CharField(max_length=25)
    instructor_email = models.CharField(max_length=25)
    instructor_username = models.CharField(max_length=25)
    instructor_password = models.CharField(max_length=30) # TODO: Hash this
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instructor_name


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=25)
    admin_email = models.CharField(max_length=25)
    admin_username = models.CharField(max_length=25)
    admin_password = models.CharField(max_length=30) # TODO: Hash this
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin_name
    

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket_title


class Class(models.Model):
    group_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=25)
    class_instructor = models.OneToOneField(Instructor, on_delete=models.DO_NOTHING) # One class group has one instructor
    class_student = models.ManyToManyField(Student) # N students can be a part of M classes
    class_join_code = models.CharField(unique=True, max_length=5, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.class_name



class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=25)
    project_instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    group_id = models.ManyToManyField(Class) # Many projects linked to many class groups
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_title


class Roadmap(models.Model):
    roadmap_id = models.AutoField(primary_key=True)
    roadmap_title = models.CharField(max_length=25)
    roadmap_description = models.TextField()
    roadmap_students = models.ManyToManyField(Student) # One student can have many roadmaps, and one roadmap can have many students
    created_at = models.DateTimeField(auto_now_add=True)

    metadata = models.JSONField(default=dict)

    def __str__(self):
        return self.roadmap_title


class Attachment(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    attachment_roadmap = models.ForeignKey(Roadmap, on_delete=models.DO_NOTHING) # One roadmap has many attachments
    attachment_name = models.CharField(max_length=75)

    attachment_metadata = models.FileField(null=True)

    def __str__(self):
        return self.attachment_name