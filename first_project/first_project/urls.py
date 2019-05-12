"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app.views import *

urlpatterns = [
    path('read_data', read_data),
    path('save_data', save_data),
    path('calc', calc),
    path('read_book_data', read_book_data, name='read_book_data'),
    path('save_book_data', save_book_data, name='save_book_data'),
    path('search_book_data', search_book_data, name='search_book_data'),
    path('update_book_data', update_book_data, name='update_book_data'),
    path('delete_book_data', delete_book_data, name='delete_book_data'),
    path('edit_book_data', edit_book_data, name='edit_book_data'),
    path('', say_hello),
]
