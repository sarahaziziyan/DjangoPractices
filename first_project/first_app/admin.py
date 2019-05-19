from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Session)