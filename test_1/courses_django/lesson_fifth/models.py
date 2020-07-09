from django.db import models

# Create your models here.

class Author1(models.Model):

    CHOICES_FOR_CITY = {
        ('kyiv', 'Киев'),
        ('chernigov', 'Чернигов'),
        ('odessa', 'Одесса'),
        ('lvov', 'Львов'),
    }
    name    = models.CharField(max_length=200, verbose_name='Имья автора',)
    surname = models.CharField(max_length=200, verbose_name='Фамилия автора')
    city    = models.CharField(choices=CHOICES_FOR_CITY, max_length=200, blank=False, verbose_name='Город', help_text='Выбирите город со списка') # если blank=False,
    # тогда выбор города будет обьязательным и форма не будет отправлятся.

    def __str__(self):
        return 'Имя %s' % self.name


class Article(models.Model):
    author  = models.ForeignKey(Author1, on_delete=models.CASCADE, verbose_name='Автор статьи')
    title   = models.CharField(max_length=100, verbose_name='Заголовок')
    text    = models.TextField(max_length=500, verbose_name='Текст статьи')

    def __str__(self):
        return self.title

# сделать миграцию !!!