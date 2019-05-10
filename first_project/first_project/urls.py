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
    path('read_library_data', read_library_data),
    path('save_library_data', save_library_data),
    path('search_library_data', search_library_data),
    path('update_library_data', update_library_data, name='update_library_data'),
    path('delete_library_data', delete_library_data),
    path('edit_library_data', edit_library_data, name='edit_library_data'),
    path('', say_hello),
]
