from django.contrib import admin

# Register your models here.
from .models import Userfile,Pack


admin.site.register(Userfile)
admin.site.register(Pack)
