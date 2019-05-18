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


class Product(models.Model):
    productId = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=128)
    price = models.IntegerField()
    inventory = models.IntegerField()
    image= models.ImageField(upload_to='products')
    date_made = models.DateField()
    type = models.CharField(max_length=1, choices=[['C', 'CellPhones'], ['T', 'Television'], ['C', 'Computer']], default='C')

    def __str__(self):
        return self.title


class Customer(models.Model):
    nationalCode = models.CharField(max_length=10, primary_key=True)
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    product = models.ManyToManyField(Product, through='Buy')


class Buy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    buy_date = models.DateField(default=now())
    count = models.CharField(max_length=64)
