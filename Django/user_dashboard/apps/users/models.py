from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = []
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Invalid email address')
        if self.filter(email = postData['email']):
            errors.append('email already in use')
        if len(postData['email']) == 0 or len(postData['email']) < 4:
            errors.append('email must be 4 characters long')
        if len(postData['first_name']) < 2 or len(postData['first_name']) == 0:
            errors.append('First name must be longer than 2 characters')
        if not postData['first_name'].isalpha():
            errors.append('First name can only contain letters')
        if len(postData['last_name']) < 2 or len(postData['last_name']) == 0:
            errors.append('Last name must be longer than 2 characters')
        if not postData['last_name'].isalpha():
            errors.append('Last name can only contain letters')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters longs')
        if postData['password'] != postData['password_confirm']:
            errors.append('Passwords do not match')
        return errors

    def create_user(self, cleanData):
        hashed = bcrypt.hashpw(cleanData['password'].encode(), bcrypt.gensalt())
        if User.objects.first():
            user_level = 9
        else:
            user_level = 0
        return self.create(
            email = cleanData['email'],
            first_name = cleanData['first_name'],
            last_name = cleanData['last_name'],
            password = hashed,
            user_level = 0
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
        return errors, user

    def validate_edit(self, postData):
        errors = []
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Invalid email address')
        if self.filter(email = postData['email']):
            errors.append('email already in use')
        if len(postData['email']) == 0 or len(postData['email']) < 4:
            errors.append('email must be 4 characters long')
        if len(postData['first_name']) < 2 or len(postData['first_name']) == 0:
            errors.append('First name must be longer than 2 characters')
        if not postData['first_name'].isalpha():
            errors.append('First name can only contain letters')
        if len(postData['last_name']) < 2 or len(postData['last_name']) == 0:
            errors.append('Last name must be longer than 2 characters')
        if not postData['last_name'].isalpha():
            errors.append('Last name can only contain letters')
        return errors

    def edit_info(self, cleanData, user_id):
        user = User.objects.get(id=user_id)
        print user.first_name
        user.email = cleanData['email']
        user.first_name = cleanData['first_name']
        user.last_name = cleanData['last_name']
        user.user_level = cleanData['user_level']
        user.save()

    def validate_password_edit(self, postData):
        errors = []
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters longs')
        if postData['password'] != postData['password_confirm']:
            errors.append('Passwords do not match')
        return errors

    def update_password(self, cleanData, user_id):
        user = User.objects.get(id=user_id)
        hashed = bcrypt.hashpw(cleanData['password'].encode(), bcrypt.gensalt())
        user.password = hashed
        user.save()



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField(default=0)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
