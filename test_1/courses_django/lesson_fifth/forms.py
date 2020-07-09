from django.core.validators import URLValidator
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


class UrlForm(forms.Form):
    title = forms.CharField(label='Название сайта')
    url = forms.CharField(label="Адрес сайта")

    def clean(self):
        clean_data = super(UrlForm, self).clean()

    URLValidator
    def clean_url(self):
        url = self.cleaned_data['url']
        validation_url = URLValidator()
        try:
            validation_url(url)
        except:
            raise forms.ValidationError('Это не адрес сайта!')
        return url