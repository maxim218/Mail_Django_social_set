from django.db import models
from django.utils import timezone

class MyUsers(models.Model):
    user_login = models.TextField()
    user_password = models.TextField()

    def __str__(self):
        return self.user_login

class MyUsersInfo(models.Model):
    user_login = models.TextField()
    user_s1 = models.TextField()
    user_s2 = models.TextField()
    user_s3 = models.TextField()

    def __str__(self):
        return self.user_login


class MyRecords(models.Model):
    user_login = models.TextField()
    user_record = models.TextField()

    def __str__(self):
        return self.user_login