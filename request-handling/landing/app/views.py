from collections import Counter

# from django.http import HttpResponse
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()

front_types = {
    'original': 'landing.html',
    'test': 'landing_alternate.html',
}


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    transition_type = request.GET.get('from-landing')
    if transition_type is not None:
        counter_click[transition_type] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    front_type = request.GET.get('ab-test-arg')
    counter_show[front_type] += 1
    return render_to_response(front_types[front_type])


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    if counter_show['test'] == 0:
        test_ratio = counter_click['test']
    else:
        test_ratio = counter_click['test'] / counter_show['test']

    if counter_show['original'] == 0:
        original_ratio = counter_click['original']
    else:
        original_ratio = counter_click['original'] / counter_show['original']

    return render_to_response('stats.html', context={
        'test_conversion': f'{test_ratio:.{1}f}',
        'original_conversion': f'{original_ratio:.{1}f}',
    })
