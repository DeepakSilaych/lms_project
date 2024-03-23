from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    profile_picture_url = models.URLField(blank=True)
    
    groups = models.ManyToManyField( #to fix django error
        'auth.Group',
        related_name='lms_users',
        blank=True,
        help_text='The groups this user belongs to. A user can belong to multiple groups.')

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='lms_users',
        blank=True,
        help_text='Specific permissions for this user.')


class Class(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes')
    students = models.ManyToManyField(User, related_name='enrolled_classes', blank=True)
    start_date = models.DateField()
    description = models.TextField(blank=True)
    subject = models.CharField(max_length=255, blank=True) 

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    cls = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='assignments')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_assignments')
    max_points = models.IntegerField(default=100)  
    submission_type = models.CharField(max_length=255, choices=(('text', 'Text'), ('file_upload', 'File Upload')), default='text')  

class Question(models.Model):
    text = models.TextField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=255, choices=(('multiple_choice', 'Multiple Choice'), ('true_false', 'True/False'), ('subjective', 'Subjective')), default='open_ended')
