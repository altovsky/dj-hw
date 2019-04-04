from django.contrib import admin

# Register your models here.
from .models import Phone, Xiaomi, Motorola, Alcatel

admin.site.register(Phone)
admin.site.register(Xiaomi)
admin.site.register(Motorola)
admin.site.register(Alcatel)
