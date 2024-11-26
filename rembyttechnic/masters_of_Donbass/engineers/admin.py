from django.contrib import admin
from .models import Engineer

class EngineerAdmin(admin.ModelAdmin):
    list_display = ('name', 'i_info', 'username', 'email', 'created')


admin.site.register(Engineer, EngineerAdmin)