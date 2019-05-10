from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


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


def read_library_data(request):
    return render(request, 'library.html', {'rows': Library.objects.all()})


def save_library_data(request):
    new_ins = Library(title=request.POST['title'], author=request.POST['author'], price=request.POST['price'])
    new_ins.save()
    return read_library_data(request)


def search_library_data(request):
    return render(request, 'library.html',
                  {'rows': Library.objects.filter(title=request.POST['title'])})


# def update_library_data(request):
#     inst = Library.objects.get(title=request.POST['title'])
#     inst.author = request.POST['author']
#     inst.price  = request.POST['price']
#     inst.save()
#     return read_library_data(request)

def delete_library_data(request):
    Library.objects.get(title=request.POST['title']).delete()
    return read_library_data(request)


def edit_library_data(request):
    ins = Library.objects.get(title=request.POST['title'])
    form = LibraryForm(instance=ins)
    return render(request,'EditForm.html',{'form' : form , 'unique':request.POST['title']})

def update_library_data(request):
    ins = Library.objects.get(title=request.POST['unique'])
    form = LibraryForm(data=request.POST, instance=ins)
    form.save()
    return read_library_data(request)