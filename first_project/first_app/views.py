from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from string import *


def say_hello(request):
    return HttpResponse('Hello World!!!')


def calc(request):
    if request.POST:
        methodName = request.POST['methodName']
        n1 = request.POST['number1']
        n2 = request.POST['number2']
        code = 0
        msg = ''
        result = 0
        res = ''
        if validateRequestParams(n1, n2):
            n1 = float(n1)
            n2 = float(n2)
            if (methodName == 'add'):
                result = n1 + n2
            elif (methodName == 'subtract'):
                result = n1 - n2
            elif (methodName == 'multiply'):
                result = n1 * n2
            elif (methodName == 'divide'):
                result = n1 / n2
            else:
                code = 1
                msg = 'method does not exist'
        else:
            code = 2
            msg = 'invalid parameters'

        res = "<info>" \
                "<code>" + str(code) + "</code>" \
                "<msg>" + msg + "</msg>" \
                "<mydata>" \
                    "<result>" + str(result) + "</result>" \
                "</mydata>" \
              "</info>"
        return HttpResponse(res)
    return render(request, 'calc.html', {})


def validateRequestParams(n1, n2):
    if n1.isdigit() != True or n2.isdigit() != True:
        return False
    else:
        return True


def read_data(request):
    return render(request, 'phone_book.html', {'rows': PhoneBook.objects.all()})


def save_data(request):
    new_ins = PhoneBook(name=request.POST['name'], phone=request.POST['phone'])
    new_ins.save()
    return read_data(request)
