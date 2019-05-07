from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def say_hello(request):
    return HttpResponse('Hello World!!!')


def calc(request):
   return render(request, 'calc.html', {})


def add(request):
    n1 = float(request.POST['number1'])
    n2 = float(request.POST['number2'])
    sum = n1 + n2
    d1 = "<info>" \
            "<mydata>" \
                "<sum>"+str(sum)+"</sum>" \
            "</mydata>" \
         "</info>"
    return HttpResponse(d1)


def read_data(request):
    return render(request, 'phone_book.html', {'rows': PhoneBook.objects.all()})

def save_data(request):
    new_ins = PhoneBook(name=request.POST['name'], phone=request.POST['phone'])
    new_ins.save()
    return read_data(request)