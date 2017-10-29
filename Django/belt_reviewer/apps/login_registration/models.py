from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = []
        if len(postData['name']) < 2 or len(postData['name']) == 0:
            errors.append('Name must be longer than 2 characters')
        if len(postData['alias']) < 2 or len(postData['alias']) == 0:
            errors.append('Alias must be longer than 2 characters')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Invalid email address')
        if self.filter(email = postData['email']):
            errors.append('email already in use')
        if len(postData['email']) == 0:
            errors.append('email can not be empty')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters longs')
        if postData['password'] != postData['pass_confirm']:
            errors.append('Passwords do not match')
        return errors

    def create_user(self, cleanData):
        hashed = bcrypt.hashpw(cleanData['password'].encode(), bcrypt.gensalt())
        return self.create(
            name = cleanData['name'],
            alias = cleanData['alias'],
            email = cleanData['email'],
            password = hashed
        )

    def validate_login(self, postData):
        errors = []
        user = None
        if self.filter(email = postData['email']):
            user = self.get(email = postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors.append('Incorrect username/password')
                user = None
        else:
            errors.append('Incorrect username/password')
            user = None
        return (errors, user)

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
