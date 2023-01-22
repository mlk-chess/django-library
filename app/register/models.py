# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    CLIENT = 'CLIENT'
    BOOKSELLER = 'BOOKSELLER'
    ROLE_CHOICES = (
        (BOOKSELLER, 'bookseller_role'),
        (CLIENT, 'client_role'),
    )

    lastname = models.CharField(max_length=255, verbose_name='Lastname', null=False, default=None, blank=True)
    firstname = models.CharField(max_length=255, verbose_name='firstname', null=False, default=None, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Role')
    locationLibrary = models.CharField(max_length=255, verbose_name='Location of the library', null=True, default=None, blank=True)
    age = models.IntegerField(verbose_name='Age', null=True, default=None, blank=True)
    description = models.TextField(verbose_name='Description', null=True, default=None, blank=True)

