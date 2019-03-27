from django import template

import datetime

register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    then = datetime.datetime.fromtimestamp(value)
    delta = datetime.datetime.now() - then
    delta_minutes = delta.seconds / 60  # Минуты
    delta_hours = delta.seconds / 3600  # Часы

    if delta_minutes < 10:
        ret_value = 'только что'
    elif delta_hours < 24:
        ret_value = f'{delta.seconds // 3600} часов назад'
    else:
        ret_value = f'{then.year}-{then.month}-{then.date()}'

    return ret_value


# необходимо добавить фильтр для поля `score`
@register.filter
def score_derivative(value, default_value):

    if not value:
        value = default_value

    if value < 5:
        ret_value = 'все плохо'
    elif -5 <= value < 5:
        ret_value = 'нейтрально'
    else:
        ret_value = 'хорошо'

    return ret_value


@register.filter
def format_num_comments(value):
    # Ваш код
    if value == 0:
        ret_value = 'Оставьте комментарий'
    elif 0 < value < 50:
        ret_value = value
    else:
        ret_value = '50+'

    return ret_value


@register.filter
def format_selftext(value, count):

    split_value = value.split(' ')
    split_len = len(split_value)
    if split_len > count:
        left_val = ''
        right_val = ''
        left = split_value[:count]
        right = split_value[(split_len-count):split_len]

        for i in left:
            left_val += f'{i} '

        for i in right:
            right_val += f'{i} '

        ret_value = f'{left_val}...{right_val}'

    else:
        ret_value = value

    return ret_value
