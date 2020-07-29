from django.db import models
import bcrypt
import re

# Create your models here.

class UserManager(models.Manager):

    def validations(self, form_data):
        pass

    def register(self, form_data):
        hash1 = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt()).decode()
        self.create (
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            username = form_data['username'],
            password = hash1
        )

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
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
    message = models.ForeignKey(User, related_name='comments_in_message', on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)