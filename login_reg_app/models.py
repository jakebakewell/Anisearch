from django.db import models
from datetime import date, datetime
import re
import bcrypt
from dateutil.relativedelta import relativedelta

class UserManager(models.Manager):
    def registration_validator(self, post_data):
        errors = {}
        if len(post_data['username']) < 1:
            errors["username"] = "Cannot register without a username."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address."
        registration_email = User.objects.filter(email=post_data['email'])
        if len(registration_email) > 0:
            errors["multiple_emails"] = "A user is all ready using that email."
        if len(post_data['birthday']) == 0:
            errors['no_birthday'] = "Must fill out birthday."
        else:
            user_birthday = datetime.strptime(post_data['birthday'], '%Y-%m-%d')
            if user_birthday > datetime.today():
                errors["birthday_future"] = "User birthday must be in the past."
            if user_birthday > datetime.today() - relativedelta(years=13):
                errors["not_old_enough"] = "User must be at least 13."
        if len(post_data['password']) < 8:
            errors["password"] = "Password must be at least 8 characters."
        if not post_data['password'] == post_data['password_confirm']:
            errors["password_confirm"] = "Passwords must match."
        return errors
    def login_validator(self, post_data):
        errors_login = {}
        user = User.objects.filter(email=post_data['email_login'])
        if len(user) == 0:
            errors_login["email_login"] = "No user associated with that email!"
        else:
            logged_user = user[0]
            user_password = logged_user.password
            if not bcrypt.checkpw(post_data['password_login'].encode(), user_password.encode()):
                errors_login["password_login"] = "Password does not match the one on file!"
        return errors_login

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    birthday = models.DateField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
