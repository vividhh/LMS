from django.contrib import admin
from .models import Books, Orders, Member

# Register your models here.
admin.site.register([Books, Orders, Member])