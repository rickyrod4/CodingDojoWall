from django.db import models
import bcrypt
import re

# Create your models here.

class UserManager(models.Manager):

    def validations(self, form_data):
        errors = {}
        if len(form_data['first_name']) < 1:
            errors['first_name'] = "First Name Field is Required"

        if len(form_data['last_name']) < 1:
            errors['last_name'] = "Last Name Field is Required"

        if len(form_data['username']) < 1:
            errors['username'] = "Username Field is Required"
        
        if len(form_data['password']) < 1:
            errors['password'] = "Please enter a password"

        if len(form_data['confirmPassword']) < 1:
            errors['confirmPassword'] = "Please confirm your password"

        if form_data['password'] != form_data['confirmPassword']:
            errors['confrimPassword'] = "Passwords do not match"

        return errors

    def register(self, form_data):
        hash1 = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt()).decode()
        self.create (
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            username = form_data['username'],
            password = hash1
        )

    def authenticate(self, name, password):
        users_with_username = self.filter(username=name)
        if not users_with_username:
            return False
        user = users_with_username[0]
        return bcrypt.checkpw(password.encode(),user.password.encode())


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    #messages
    #comments

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()



class Message(models.Model):
    message = models.TextField()
    author = models.ForeignKey(User, related_name='messages', on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments_in_message', on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)