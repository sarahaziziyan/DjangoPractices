from django.db import models
from django.db.models import *
from django.utils.timezone import now


class PhoneBook(Model):
    name = CharField(max_length=50)
    phone = CharField(max_length=50)


class Book(Model):
    title = CharField(max_length=50, verbose_name='عنوان')
    author = CharField(max_length=50, verbose_name='نویسنده')
    price = CharField(max_length=50, verbose_name='قیمت')


class Borrower(Model):
    firstName = CharField(max_length=50, verbose_name='نام')
    lastName = CharField(max_length=50, verbose_name='نام خانوادگی')
    Book = models.ManyToManyField(Book, through='Book_Borrower')


class Book_Borrower(Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.ForeignKey(Borrower, on_delete=models.PROTECT)
    date_borrow = models.DateField(default=now())
    time_borrow = models.TimeField(default=now())
