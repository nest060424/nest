from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput
from .models import Category, Department, Person, Status, Statement, Kind, Position, Employee, Queue, History, News 
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# При разработке приложения, использующего базу данных, чаще всего необходимо работать с формами, которые аналогичны моделям.
# В этом случае явное определение полей формы будет дублировать код, так как все поля уже описаны в модели.
# По этой причине Django предоставляет вспомогательный класс, который позволит вам создать класс Form по имеющейся модели
# атрибут fields - указание списка используемых полей, при fields = '__all__' - все поля
# атрибут widgets для указания собственный виджет для поля. Его значением должен быть словарь, ключами которого являются имена полей, а значениями — классы или экземпляры виджетов.

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={"size":"100"}),            
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={"size":"100"}),            
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('sex', 'iin', 'birthday', 'surname', 'name', 'patronymic')
        widgets = {
            'iin': TextInput(attrs={"size":"50"}),
            'birthday': DateInput(attrs={"type":"date"}),
            'surname': TextInput(attrs={"size":"100"}),
            'name': TextInput(attrs={"size":"100"}),
            'patronymic': TextInput(attrs={"size":"100"}),
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={"size":"100"}),            
        }

class StatementCreateForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ('dates', 'person', 'category', 'kind1', 'paper1', 'kind2', 'paper2', 'kind3', 'paper3', 'kind4', 'paper4', 'kind5', 'paper5', 'kind6', 'paper6', 'kind7', 'paper7')
        widgets = {
            'dates': DateInput(attrs={"type":"date", "readonly":"readonly"}),
            'person': forms.Select(attrs={"disabled": "true"}),
            'category': forms.Select(attrs={'class': 'chosen'}),
            'kind1': forms.Select(attrs={'class': 'chosen'}),
            'kind2': forms.Select(attrs={'class': 'chosen'}),
            'kind3': forms.Select(attrs={'class': 'chosen'}),
            'kind4': forms.Select(attrs={'class': 'chosen'}),
            'kind5': forms.Select(attrs={'class': 'chosen'}),
            'kind6': forms.Select(attrs={'class': 'chosen'}),
            'kind7': forms.Select(attrs={'class': 'chosen'}),            
        }
        labels = {
            'person': _('person'),
            'category': _('category'),
            'kind1': _('kind'),
            'kind2': _('kind'),
            'kind3': _('kind'),
            'kind4': _('kind'),
            'kind5': _('kind'),
            'kind6': _('kind'),
            'kind7': _('kind'),
        }


class StatementSubscribeForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ('dates', 'person', 'category')
        widgets = {
            'dates': DateInput(attrs={"type":"date", "readonly":"readonly"}),
            'person': forms.Select(attrs={"disabled": "true"}),
            'category': forms.Select(attrs={"disabled": "true"}),
        }
        
class StatementEditForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ('dates', 'person', 'category', 'kind1', 'paper1', 'kind2', 'paper2', 'kind3', 'paper3', 'kind4', 'paper4', 'kind5', 'paper5', 'kind6', 'paper6', 'kind7', 'paper7')
        widgets = {
            'dates': DateInput(attrs={"type":"date", "readonly":"readonly"}),
            'person': forms.Select(attrs={"disabled": "true"}),
            'category': forms.Select(attrs={'class': 'chosen'}),
            'kind1': forms.Select(attrs={'class': 'chosen'}),
            'kind2': forms.Select(attrs={'class': 'chosen'}),
            'kind3': forms.Select(attrs={'class': 'chosen'}),
            'kind4': forms.Select(attrs={'class': 'chosen'}),
            'kind5': forms.Select(attrs={'class': 'chosen'}),
            'kind6': forms.Select(attrs={'class': 'chosen'}),
            'kind7': forms.Select(attrs={'class': 'chosen'}),            
        }


class StatementCheckForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ('dates', 'person', 'category', 'examination', 'datee')
        widgets = {
            'dates': DateInput(attrs={"type":"date", "readonly":"readonly"}),
            'person': forms.Select(attrs={"disabled": "true"}),
            'category': forms.Select(attrs={"disabled": "true"}),
            'examination': forms.Select(attrs={"disabled": "true"}),
            'datee': DateInput(attrs={"type":"date", "readonly":"readonly"}),
        }

class QueueEditForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = ('dateq2', 'details2')
        widgets = {
            'dateq2': DateInput(attrs={"type":"date"}),
            'details2': Textarea(attrs={'cols': 80, 'rows': 10}),            
        }
        
class KindForm(forms.ModelForm):
    class Meta:
        model = Kind
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={"size":"100"}),            
        }

"""        
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('request', 'kind', 'paper')
        widgets = {
            'kind': forms.Select(attrs={'class': 'chosen'}),
        }
        exclude = ('primary',)
"""

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={"size":"100"}),            
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('surname', 'name', 'patronymic', 'department', 'position', 'signature')
        widgets = {
            'surname': TextInput(attrs={"size":"100"}),
            'name': TextInput(attrs={"size":"100"}),
            'patronymic': TextInput(attrs={"size":"100"}),
            'department': forms.Select(attrs={'class': 'chosen'}),
            'position': forms.Select(attrs={'class': 'chosen'}),
            'signature': DateInput(attrs={"type":"number"}),
        }
        labels = {
            'department': _('department'),
            'position': _('position'),
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('daten', 'title', 'details', 'photo')
        widgets = {
            'daten': DateInput(attrs={"type":"date"}),
            'title': TextInput(attrs={"size":"100"}),
            'details': Textarea(attrs={'cols': 80, 'rows': 10}),            
        }


# Форма регистрации
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
