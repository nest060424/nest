"""nest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  re_path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings 
from django.conf.urls.static import static 
from django.conf.urls import include

from sequence import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('faq/', views.faq, name='faq'),
    path('link/', views.link, name='link'),
    path('contact/', views.contact, name='contact'),
    path('report/', views.report, name='report'),        
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    path('category/index/', views.category_index, name='category_index'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:id>/', views.category_delete, name='category_delete'),
    path('category/read/<int:id>/', views.category_read, name='category_read'),
    
    path('department/index/', views.department_index, name='department_index'),
    path('department/create/', views.department_create, name='department_create'),
    path('department/edit/<int:id>/', views.department_edit, name='department_edit'),
    path('department/delete/<int:id>/', views.department_delete, name='department_delete'),
    path('department/read/<int:id>/', views.department_read, name='department_read'),

    path('position/index/', views.position_index, name='position_index'),
    path('position/create/', views.position_create, name='position_create'),
    path('position/edit/<int:id>/', views.position_edit, name='position_edit'),
    path('position/delete/<int:id>/', views.position_delete, name='position_delete'),
    path('position/read/<int:id>/', views.position_read, name='position_read'),

    path('employee/index/', views.employee_index, name='employee_index'),
    #path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/edit/<int:id>/', views.employee_edit, name='employee_edit'),
    #path('employee/delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('employee/read/<int:id>/', views.employee_read, name='employee_read'),

    path('person/index/', views.person_index, name='person_index'),
    #path('person/create/', views.person_create, name='person_create'),
    #path('person/edit/<int:id>/', views.person_edit, name='person_edit'),
    path('person/edit/', views.person_edit, name='person_edit'),
    #path('person/delete/<int:id>/', views.person_delete, name='person_delete'),
    path('person/read/<int:id>/', views.person_read, name='person_read'),    

    path('status/index/', views.status_index, name='status_index'),
    path('status/create/', views.status_create, name='status_create'),
    path('status/edit/<int:id>/', views.status_edit, name='status_edit'),
    path('status/delete/<int:id>/', views.status_delete, name='status_delete'),
    path('status/read/<int:id>/', views.status_read, name='status_read'),

    path('statement/index/', views.statement_index, name='statement_index'),
    path('statement/list/', views.statement_list, name='statement_list'),
    path('statement/create/', views.statement_create, name='statement_create'),
    path('statement/edit/<int:id>/', views.statement_edit, name='statement_edit'),
    path('statement/subscribe/<int:id>/', views.statement_subscribe, name='statement_subscribe'),
    path('statement/check/<int:id>/', views.statement_check, name='statement_check'),
    path('statement/read/<int:id>/', views.statement_read, name='statement_read'),

    path(r'^export/word/$', views.export_word, name='export_word'),
    
    path('queue/index/', views.queue_index, name='queue_index'),
    path('queue/list/', views.queue_list, name='queue_list'),
    path('queue/edit/<int:id>/', views.queue_edit, name='queue_edit'),
    path('queue/read/<int:id>/', views.queue_read, name='queue_read'),

    path('kind/index/', views.kind_index, name='kind_index'),
    path('kind/create/', views.kind_create, name='kind_create'),
    path('kind/edit/<int:id>/', views.kind_edit, name='kind_edit'),
    path('kind/delete/<int:id>/', views.kind_delete, name='kind_delete'),
    path('kind/read/<int:id>/', views.kind_read, name='kind_read'),

    path('history/index/', views.history_index, name='history_index'),
    path('history/list/', views.history_list, name='history_list'),
    path('history/create/', views.history_create, name='history_create'),
    #path('history/edit/<int:id>/', views.history_edit, name='history_edit'),
    #path('history/delete/<int:id>/', views.history_delete, name='history_delete'),
    #path('history/read/<int:id>/', views.history_read, name='history_read'),

    path('news/index/', views.news_index, name='news_index'),
    path('news/list/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/edit/<int:id>/', views.news_edit, name='news_edit'),
    path('news/delete/<int:id>/', views.news_delete, name='news_delete'),
    path('news/read/<int:id>/', views.news_read, name='news_read'),

    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logoutUser, name="logout"),
    path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


