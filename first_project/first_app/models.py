
from django.db.models import Model, CharField


class PhoneBook(Model):
    name = CharField(max_length=50)
    phone = CharField(max_length=50)


class Library(Model):
    title = CharField(max_length=50)
    author = CharField(max_length=50)
    price = CharField(max_length=50)
