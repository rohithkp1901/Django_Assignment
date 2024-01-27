from django.contrib import admin
from .models import register
# Register your models here.
class adminname(admin.ModelAdmin):
    list_display=('firstname',)
admin.site.register(register,adminname)