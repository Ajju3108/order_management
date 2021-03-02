from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
# project model fields: project_name[char-100], text[char-256], translated_to_language[list], created_at[datetime], updated_at[datetime]
# order model fields: project_id(fk), status[choicefield- new, in-process, complete], translated_text[char-256], created_at[datetime], updated_at[datetime]
# notification model fields: user_id(fk), text[char-256], is_read[boolean], created_at[datetime], updated_at[datetime]


class Users(User):
    
    mobile = models.BigIntegerField()
    date_of_birth = models.DateField(default=None)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

class Notification(models.Model):
    text = models.CharField(max_length=256)
    is_read = models.BooleanField()
    usersid = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='user_notif')
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

class Project(models.Model):
    project_name = models.CharField(max_length=20)
    text = models.CharField(max_length=256)
    translate_to_language = models.CharField(max_length=20)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='userref')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

class Order(models.Model):
    new = 'new'
    in_process = 'in_process'
    complete = 'complete'
    choices = [(new,'new'), (in_process,'in-process'), (complete,'complete')]
    status = models.CharField(max_length=25,choices=choices)
    translated_text = models.CharField(max_length=256)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='projectref')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

    def is_upperclass(self):
        return self.status in {self.new, self.in_process,self.complete}