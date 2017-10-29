from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, postData):
        errors = []
        if len(postData['name']) < 10:
            errors.append('course title must be longer than 10 characters')
        if len(postData['description']) < 15:
            errors.append('description must be longer than 15 characters')
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
