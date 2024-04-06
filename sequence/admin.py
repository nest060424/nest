from django.contrib import admin

from .models import Category, Department, Person, Status, Statement, Kind, Position, Employee, Queue, History, News 

# Добавление модели на главную страницу интерфейса администратора
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Person)
admin.site.register(Status)
admin.site.register(Statement)
admin.site.register(Kind)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Queue)
admin.site.register(History)
admin.site.register(News)
