from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Subject, Scope


class SubjectInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form_data = form.cleaned_data
            if not len(form_data):
                continue
            if form_data['main']:
                main_count += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')

        if main_count == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_count > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class SubjectInline(admin.TabularInline):
    model = Subject
    formset = SubjectInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # pass
    inlines = [SubjectInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
