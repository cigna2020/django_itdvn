from django import template
import datetime


register = template.Library()

@register.filter(name='my_lower_filter')
def my_lower_filter(value):   # Only one arguments
    return value.lower()

@register.filter(name='compare_number')
def compare_number(value):
    if value == 0:
        return 'ZERO!'
    elif 0 < value < 10:
        return 'The number from 0 to 10'
    elif 10 < value < 50:
        return 'The number from 10 to 50'
    else:
        return 'The number greater than 50!'

@register.filter(name='get date color')
def get_due_date_color(value):
    if value == 0:
        return 'red!'
    elif 0 < value < 10:
        return 'green'
    elif 10 < value < 50:
        return 'blue'
    else:
        return 'black'
# таким образом записыватеся СОБСТВЕННЫЙ ТЕГ. "minusone" - это значение тега.
# что-бы тег работал в html файл нужно поключить лоад: {% load poll_extras %}
register.simple_tag(lambda x: x-1, name='minusone')

@register.simple_tag(name='minustwo')
def some_function(value):
    return value - 2
