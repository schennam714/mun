from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Next_Conf

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Next_Conf)
