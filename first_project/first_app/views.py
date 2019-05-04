from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    return HttpResponse('Hello World!!!')


def calc(request):
    n1 = request.POST['num1']
    n2 = request.POST['num2']
    sum = n1+n2
    return render(request, 'calc.html', {'sum':sum})
