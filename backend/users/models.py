from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Now

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student','Student'),
        ('instructor','Instructor'),
        ('admin','Admin'),
    )

    role = models.CharField(max_length=12,choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def isStudent(self):
        return self.role == 'student'
    
    @property
    def isInstructor(self):
        return self.role == 'instructor'

    def __str__(self):
        return self.get_full_name()


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')

    def __str__(self):
        return self.user.get_full_name()
    
class Instructor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='instructor')
    bio = models.TextField(blank=True,null=True)
    expertise = models.CharField(max_length=255)
    is_approved = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.user.get_full_name()