from django.contrib import admin
from .models import Techmuncommittee, Commtype, Chair
# Register your models here.

admin.site.register(Techmuncommittee)
admin.site.register(Commtype)
admin.site.register(Chair)