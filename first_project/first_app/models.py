
from django.db.models import Model, CharField


class PhoneBook(Model):
    name = CharField(max_length=50)
    phone = CharField(max_length=50)


class Library(Model):
    title = CharField(max_length=50, verbose_name='عنوان')
    author = CharField(max_length=50, verbose_name='نویسنده')
    price = CharField(max_length=50, verbose_name='قیمت')
