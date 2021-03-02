from django.contrib import admin
from .models import *

# Register your models here.

class notification_admin(admin.ModelAdmin):
    list_display = ['text','is_read','created_on','updated_on']

class User_admin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','username','mobile','date_of_birth','created_on','updated_on']

class project_admin(admin.ModelAdmin):
    list_display = ['project_name','text','translate_to_language','user','created_on','updated_on']


class Orde_admin(admin.ModelAdmin):
    list_display = ['choices','status','translated_text','project','created_on','updated_on']


admin.site.register(Users,User_admin)
admin.site.register(Notification,notification_admin)
admin.site.register(Project,project_admin)
admin.site.register(Order,Orde_admin)
