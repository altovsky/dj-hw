import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import os


class FileList(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

        if date:
            date = date[:10]
            file_datetime = datetime.datetime.strptime(date[:10], '%Y-%m-%d')

        file_list = os.listdir(f'{settings.FILES_PATH}')
        file_info_list = []

        for file in file_list:
            file_stat = os.stat(os.path.join(settings.FILES_PATH, file))
            file_info = {
                'name': file,
                'ctime': datetime.datetime.fromtimestamp(file_stat.st_ctime),
                'mtime': datetime.datetime.fromtimestamp(file_stat.st_mtime),
            }

            # print('!!!!!', date, datetime.date.fromtimestamp(file_stat.st_ctime))
            print('!!!!!', date, file_info['ctime'])
            if date:
                if file_datetime.date() == file_info['ctime'].date():
                    file_info_list.append(file_info)
            else:
                file_info_list.append(file_info)

        return {
            'files': file_info_list,
            'date': date,  # Этот параметр необязательный
        }


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    with open(os.path.join(settings.FILES_PATH, name), 'r', encoding='utf-8') as server_file:
        server_file_content = server_file.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': f'{name}', 'file_content': server_file_content}
    )
