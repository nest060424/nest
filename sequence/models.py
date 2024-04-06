from django.db import models
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from django.core.files.storage import default_storage as storage  

from django.contrib.auth.models import User

# Модели отображают информацию о данных, с которыми вы работаете.
# Они содержат поля и поведение ваших данных.
# Обычно одна модель представляет одну таблицу в базе данных.
# Каждая модель это класс унаследованный от django.db.models.Model.
# Атрибут модели представляет поле в базе данных.
# Django предоставляет автоматически созданное API для доступа к данным

# choices (список выбора). Итератор (например, список или кортеж) 2-х элементных кортежей,
# определяющих варианты значений для поля.
# При определении, виджет формы использует select вместо стандартного текстового поля
# и ограничит значение поля указанными значениями.

# Читабельное имя поля (метка, label). Каждое поле, кроме ForeignKey, ManyToManyField и OneToOneField,
# первым аргументом принимает необязательное читабельное название.
# Если оно не указано, Django самостоятельно создаст его, используя название поля, заменяя подчеркивание на пробел.
# null - Если True, Django сохранит пустое значение как NULL в базе данных. По умолчанию - False.
# blank - Если True, поле не обязательно и может быть пустым. По умолчанию - False.
# Это не то же что и null. null относится к базе данных, blank - к проверке данных.
# Если поле содержит blank=True, форма позволит передать пустое значение.
# При blank=False - поле обязательно.

# Категория учета
class Category(models.Model):
    title = models.CharField(_('title_category'), unique=True, max_length=196)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'category'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['title']),
        ]
        # Сортировка по умолчанию
        ordering = ['title']
    def __str__(self):
        # Вывод Название в тег SELECT 
        return self.title
    
# Отдел (подразделение)
class Department(models.Model):
    title = models.CharField(_('title_department'), unique=True, max_length=196)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'department'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['title']),
        ]
        # Сортировка по умолчанию
        ordering = ['title']
    def __str__(self):
        # Вывод Название в тег SELECT 
        return self.title

# Должность 
class Position(models.Model):
    title = models.CharField(_('title_position'), unique=True, max_length=96)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'position'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['title']),
        ]
        # Сортировка по умолчанию
        ordering = ['title']
    def __str__(self):
        # Вывод Название в тег SELECT 
        return self.title
    
# Сотрудник
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    surname = models.CharField(_('surname'), max_length=64)
    name = models.CharField(_('name'), max_length=64)
    patronymic = models.CharField(_('patronymic'), max_length=64, blank=True, null=True)    
    department = models.ForeignKey(Department, related_name='employee_department', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, related_name='employee_position', on_delete=models.CASCADE)
    signature = models.IntegerField(_('signature'))     # Каким по счету ставит подпись
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'employee'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['surname']),
            models.Index(fields=['name']),
            models.Index(fields=['patronymic']),
            models.Index(fields=['department']),
            models.Index(fields=['position']),
        ]
        # Сортировка по умолчанию
        ordering = ['surname', 'name', 'patronymic']        
    def __str__(self):
        # Вывод в тег Select
        return "{} {} {} ({})".format(self.surname, self.name, self.patronymic, self.user.username)
    @property
    def fio(self):
        # Возврат ФИО
        return '%s %s %s' % (self.surname, self.name, self.patronymic)
    
# Персона (человек)
class Person(models.Model):
    SEX_CHOICES = (
        ('М','М'),
        ('Ж', 'Ж'),
    )    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(_('sex'), max_length=1, choices=SEX_CHOICES, default='М')
    iin = models.CharField(_('iin'), unique=True, max_length=12)
    birthday = models.DateTimeField(_('birthday'))
    surname = models.CharField(_('surname'), max_length=64)
    name = models.CharField(_('name'), max_length=64)
    patronymic = models.CharField(_('patronymic'), max_length=64, blank=True, null=True)    
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'person'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['surname']),
            models.Index(fields=['name']),
            models.Index(fields=['patronymic']),
            models.Index(fields=['iin']),            
        ]
        # Сортировка по умолчанию
        ordering = ['surname', 'name', 'patronymic']        
    def __str__(self):
        # Вывод в тег Select
        return "{} {} {} ({})".format(self.surname, self.name, self.patronymic, self.iin)
    @property
    def fio(self):
        # Возврат ФИО
        return '%s %s %s' % (self.surname, self.name, self.patronymic)

# Статус
class Status(models.Model):
    title = models.CharField(_('title_status'), unique=True, max_length=196)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'status'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['title']),
        ]
        # Сортировка по умолчанию
        ordering = ['title']
    def __str__(self):
        # Вывод Название в тег SELECT 
        return self.title

    
# Вид документа 
class Kind(models.Model):
    title = models.CharField(_('title_kind'), unique=True, max_length=96)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'kind'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['title']),
        ]
        # Сортировка по умолчанию
        ordering = ['title']
    def __str__(self):
        # Вывод Название в тег SELECT 
        return self.title
    
# Заявка
class Statement(models.Model):
    dates = models.DateTimeField(_('dates'))
    person = models.ForeignKey(Person, related_name='statement_person', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='statement_category', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='statement_status', on_delete=models.CASCADE)
    examination = models.ForeignKey(Employee, related_name='statement_employee', blank=True, null=True, on_delete=models.CASCADE)
    datee = models.DateTimeField(_('datee'), blank=True, null=True)
    kind1 = models.ForeignKey(Kind, related_name='document1_kind', on_delete=models.CASCADE)
    paper1 = models.ImageField(_('paper'), upload_to='images/')
    kind2 = models.ForeignKey(Kind, blank=True, null=True, related_name='document2_kind', on_delete=models.CASCADE)
    paper2 = models.ImageField(_('paper'), blank=True, null=True, upload_to='images/')
    kind3 = models.ForeignKey(Kind, blank=True, null=True, related_name='document3_kind', on_delete=models.CASCADE)
    paper3 = models.ImageField(_('paper'), blank=True, null=True, upload_to='images/')
    kind4 = models.ForeignKey(Kind, blank=True, null=True, related_name='document4_kind', on_delete=models.CASCADE)
    paper4 = models.ImageField(_('paper'), blank=True, null=True, upload_to='images/')
    kind5 = models.ForeignKey(Kind, blank=True, null=True, related_name='document5_kind', on_delete=models.CASCADE)
    paper5 = models.ImageField(_('paper'), blank=True, null=True, upload_to='images/')
    kind6 = models.ForeignKey(Kind, blank=True, null=True, related_name='document6_kind', on_delete=models.CASCADE)
    paper6 = models.ImageField(_('paper'), blank=True, null=True, upload_to='images/')
    kind7 = models.ForeignKey(Kind, blank=True, null=True, related_name='document7_kind', on_delete=models.CASCADE)
    paper7 = models.ImageField(_('paper'), blank=True, null=True, upload_to='images/')
    sign1 = models.ForeignKey(Employee, blank=True, null=True, related_name='statement1_employee', on_delete=models.CASCADE)
    #sign1 = models.IntegerField(_('sign1'), blank=True, null=True)     # Подпись (одобрение №1)
    dates1 = models.DateTimeField(_('dates1'), blank=True, null=True)
    sign2 = models.ForeignKey(Employee, blank=True, null=True, related_name='statement2_employee', on_delete=models.CASCADE)
    #sign2 = models.IntegerField(_('sign2'), blank=True, null=True)     # Подпись (одобрение №2)
    dates2 = models.DateTimeField(_('dates2'), blank=True, null=True)
    sign3 = models.ForeignKey(Employee, blank=True, null=True, related_name='statement3_employee', on_delete=models.CASCADE)
    #sign3 = models.IntegerField(_('sign3'), blank=True, null=True)     # Подпись (одобрение №3)
    dates3 = models.DateTimeField(_('dates3'), blank=True, null=True)
    sign4 = models.ForeignKey(Employee, blank=True, null=True, related_name='statement4_employee', on_delete=models.CASCADE)
    #sign4 = models.IntegerField(_('sign4'), blank=True, null=True)     # Подпись (одобрение №4)
    dates4 = models.DateTimeField(_('dates4'), blank=True, null=True)
    sign5 = models.ForeignKey(Employee, blank=True, null=True, related_name='statement15employee', on_delete=models.CASCADE)
    #sign5 = models.IntegerField(_('sign5'), blank=True, null=True)     # Подпись (одобрение №5)
    dates5 = models.DateTimeField(_('dates5'), blank=True, null=True)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'statement'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['person']),
            models.Index(fields=['category']),
            models.Index(fields=['status']),            
        ]
        # Сортировка по умолчанию
        ordering = ['-dates']        
    def __str__(self):
        # Вывод в тег Select
        return "{}, {} ({})".format(self.person, self.category, self.status)

# Очередь
class Queue(models.Model):
    statement = models.ForeignKey(Statement, related_name='queue_statement', on_delete=models.CASCADE)
    dateq = models.DateTimeField(_('dateq'), auto_now_add=True)
    details = models.TextField(_('queue_details'))
    dateq2 = models.DateTimeField(_('dateq2'), blank=True, null=True)
    details2 = models.TextField(_('queue2_details'))
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'queue'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['statement']),
            models.Index(fields=['dateq']),            
        ]
        # Сортировка по умолчанию
        ordering = ['dateq']        
    def __str__(self):
        # Вывод в тег Select
        return "{}, {}".format(self.statement, self.dateq)
    
# История
class History(models.Model):
    statement = models.ForeignKey(Statement, related_name='history_statement', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='history_person', on_delete=models.CASCADE)
    dateh = models.DateTimeField(_('dateh'), auto_now_add=True)
    details = models.TextField(_('history_details'))
    employee = models.ForeignKey(Employee, blank=True, null=True, related_name='history_employee', on_delete=models.CASCADE)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'history'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['statement']),
            models.Index(fields=['dateh']),
            models.Index(fields=['employee']),            
        ]
        # Сортировка по умолчанию
        ordering = ['-dateh']        
    def __str__(self):
        # Вывод в тег Select
        return "{}, {}".format(self.request, self.dateh)

# Новости 
class News(models.Model):
    daten = models.DateTimeField(_('daten'))
    title = models.CharField(_('title_news'), max_length=256)
    details = models.TextField(_('details_news'))
    photo = models.ImageField(_('photo_news'), upload_to='images/', blank=True, null=True)    
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'news'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['daten']),
        ]
        # Сортировка по умолчанию
        ordering = ['daten']
    #def save(self):
    #    super().save()
    #    img = Image.open(self.photo.path) # Open image
    #    # resize image
    #    if img.width > 512 or img.height > 700:
    #        proportion_w_h = img.width/img.height  # Отношение ширины к высоте 
    #        output_size = (512, int(512/proportion_w_h))
    #        img.thumbnail(output_size) # Изменение размера
    #        img.save(self.photo.path) # Сохранение

