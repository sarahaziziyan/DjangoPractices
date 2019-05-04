from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    return HttpResponse('Hello World!!!')


def calc(request):
    d1 = {}
    if request.POST:
        n1 = float(request.POST['num1'])
        n2 = float(request.POST['num2'])
        sum = n1+n2
        d1['sum'] = sum
    return render(request, 'calc.html', d1)
