from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    project_image = models.ImageField(upload_to = 'projects/')
    caption = models.CharField(max_length=250)
    project_link = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
