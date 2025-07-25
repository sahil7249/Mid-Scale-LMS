from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','get_full_name','get_role']

    def get_full_name(self,obj):
        return obj.get_full_name()
    get_full_name.short_description = 'Name'

    def get_role(self,obj):
        return obj.role 
    get_role.short_description = 'Role'

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','get_full_name','get_username','get_email']

    def get_username(self,obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_full_name(self,obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Name'

    def get_email(self,obj):
        return obj.user.email
    get_email.short_description = 'Email'



admin.site.register(models.Instructor)