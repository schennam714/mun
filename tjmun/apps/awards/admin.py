from django.contrib import admin
from .models import Conference, Year, Delegation, Committee
# Register your models here.

admin.site.register(Conference)
admin.site.register(Year)
admin.site.register(Delegation)
admin.site.register(Committee)