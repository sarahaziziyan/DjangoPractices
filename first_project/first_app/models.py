from django.db import models
from django.db.models import Model, CharField


class PhoneBook(Model):
    name = CharField(max_length=50)
    phone = CharField(max_length=50)
