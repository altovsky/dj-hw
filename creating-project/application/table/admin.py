from django.contrib import admin
from .models import TableSettings, CSVPath

# Register your models here.

admin.site.register(TableSettings)
admin.site.register(CSVPath)
