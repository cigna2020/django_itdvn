from django.core.validators import URLValidator, ValidationError
from django.forms import ModelForm, Form
from . import models
from django import forms
from .models import Author1
from .models import Article
from django.http import HttpResponse

class AuthorOneForm(ModelForm):
    class Meta:
        model = Author1
        fields = ['name', 'surname', 'city']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'title', 'text']

class ContactForm(forms.Form):
    boolean_field = forms.BooleanField() # Щоб галочка булін не була обов'язкова слід використовувати NullBooleanField()
    float_field = forms.FloatField()
    name_sender = forms.CharField(max_length=100, label='Введите Ваше имя')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    sender = forms.EmailField(label='Введите Ваш имейл!')


def validate_url(value):
    validation_url = URLValidator()
    value_one_invalid = False
    value_two_invalid = False
    try:
        validation_url(value)
    except:
        value_one_invalid = True

    value_two_url = 'http://' + value
    try:
        validate_url(value_two_url)
    except:
        value_two_invalid = True
    if value_one_invalid == False and value_two_invalid == False:
        raise forms.ValidationError('Неправильный адрес сайта!')
    return value

def check_dot_com(value):
    if not '.com' in value:
        raise ValidationError('Это не адрес сайта!')

def check_itvdn(value):
    if not 'itvdn' in value:
        raise ValidationError('Это не сайт ИТВДН!')

class UrlForm(forms.Form):
    title = forms.CharField(label='Название сайта')
    url = forms.CharField(label="Адрес сайта", validators=[validate_url, check_dot_com, check_itvdn])

    # def clean(self):
    #     clean_data = super(UrlForm, self).clean()
    #
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     validation_url = URLValidator()
    #     try:
    #         validation_url(url)
    #     except:
    #         raise forms.ValidationError('Это не адрес сайта!')
    #     return url