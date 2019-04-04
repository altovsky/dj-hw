from django.contrib import admin

# Register your models here.
from phones.models import Phone

admin.site.register(Phone)


# class PhoneAdmin(admin.ModelAdmin):
#     # Поле slug будет заполнено на основе поля title
#     prepopulated_fields = {'slug': ('name',)}

# class ArticleAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
