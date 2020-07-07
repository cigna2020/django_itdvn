from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Example)
admin.site.register(models.Book)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.Waiter)
admin.site.register(models.Public)
admin.site.register(models.Artic)

class AuthorAdmin(admin.ModelAdmin):
    # list_display = ['name', 'surname', 'id'] # разделяет информация на 2 столбца
    list_display = [field.name for field in models.Author._meta.fields] #  отображать все данные
    # exclude = ['name'] # прячет поле, будет недоступно для редактирования
    # fields = ['name'] # показывать поля, будут отображатся только указанные
    list_filter = ['name'] # добавляет в админку фильтр (список)
    # search_fields = ['name', 'surname'] # добавляет строку поиска
    search_fields = [field.name for field in models.Author._meta.fields] # добавляет строку поиска
    class Meta:
        model = models.Author

admin.site.register(models.Author, AuthorAdmin) # регистрация класса Автор и выше изложенного АвторАдмин.
