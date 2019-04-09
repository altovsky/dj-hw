from django.urls import path, register_converter


from .views import FileList, file_content

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from . import converters

register_converter(converters.URLDateConverter, 'dt')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.FileList и .views.file_content
    path('', FileList.as_view(), name='file_list'),
    path('<dt:date>/', FileList.as_view(), name='file_list'),
    path('file/<str:name>', file_content, name='file_content'),
]
