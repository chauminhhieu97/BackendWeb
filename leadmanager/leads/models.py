# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


#

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime, date
import decimal


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)


class movie(models.Model):
    movieId = models.IntegerField(primary_key=True)
    title = models.TextField()
    genres = models.TextField()


class tag(models.Model):
    userId = models.IntegerField()
    movieId = models.IntegerField()
    tag = models.TextField(primary_key=True)
    timestamp = models.IntegerField(null=True)


class link(models.Model):
    movieId = models.IntegerField()
    imdbId = models.IntegerField(primary_key=True)
    tmdbId = models.IntegerField()


class rating(models.Model):
    userId = models.IntegerField()
    movieId = models.IntegerField()
    rating = models.FloatField(primary_key=True)
    timestamp = models.IntegerField(null=True)

# MANH


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    MALE = 'male'
    FEMALE = 'female'
    NA = 'NA'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NA, 'N/A'),
    ]

    gender = models.CharField(
        max_length=31,
        choices=GENDER_CHOICES,
        default=MALE
    )

    MALE = 'male'
    FEMALE = 'female'
    NA = 'NA'

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    userId = models.AutoField(primary_key=True)
    username = models.TextField(unique=True)
    password = models.TextField()
    faGenres = models.TextField(null=True)
    pointRecom = models.FloatField(null=True)
    fullname = models.TextField(null=True)
    avatar = models.TextField(null=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    timestamp = models.IntegerField(null=True)

    def get_monthly_salary(self):
        return round(self.salary * decimal.Decimal(4.35) * decimal.Decimal(len(self.schedules.all())), 2)

    monthly_salary = property(get_monthly_salary)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
