from django.contrib import admin
from .models import *
# Register your models here.

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


admin.site.register(Folder, FolderAdmin)