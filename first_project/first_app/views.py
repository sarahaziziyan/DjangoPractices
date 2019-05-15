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


def read_book_data(request):
    return render(request, 'library.html', {'rows': Book.objects.all()})


def save_book_data(request):
    new_ins = Book(title=request.POST['title'], author=request.POST['author'], price=request.POST['price'])
    new_ins.save()
    return read_book_data(request)


def search_book_data(request):
    return render(request, 'library.html',
                  {'rows': Book.objects.filter(title=request.POST['title'])})


# def update_library_data(request):
#     inst = Library.objects.get(title=request.POST['title'])
#     inst.author = request.POST['author']
#     inst.price  = request.POST['price']
#     inst.save()
#     return read_library_data(request)

def delete_book_data(request):
    Book.objects.get(title=request.POST['title']).delete()
    return read_book_data(request)


def edit_book_data(request):
    ins = Book.objects.get(title=request.POST['title'])
    form = LibraryForm(instance=ins)
    return render(request,'EditForm.html',{'form' : form , 'unique':request.POST['title']})


def update_book_data(request):
    ins = Book.objects.get(title=request.POST['unique'])
    form = LibraryForm(data=request.POST, instance=ins)
    if form.is_valid():
        form.save()
    return read_book_data(request)


def read_shop_data(request):
    customerForm = CustomerForm()
    productForm = ProductForm()
    return render(
        request,
        'shop.html',
        {
            'customerForm': customerForm,
            'productForm': productForm,
            'customerRows': Customer.objects.all(),
            'productRows': Product.objects.all()
        }
    )


def save_customer_data(request):
    form = CustomerForm()
    return render(request, 'shop.html', {'customerForm' : form })


def save_product_data(request):
    new_ins = Product(
         productId=request.POST['productId'],
         name=request.POST['name'],
         price=request.POST['price'],
         inventory=request.POST['inventory']
    )
    new_ins.save()
    return read_shop_data(request)
