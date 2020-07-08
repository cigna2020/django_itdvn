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
    boolean_field = forms.BooleanField()
    float_field = forms.FloatField()
    name_sender = forms.CharField(max_length=100, label='Введите Ваше имя')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    sender = forms.EmailField(label='Введите Ваш имейл!')