"""TodoListOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from TodoListApp.views import loadTask
from TodoListApp.views import addTaskRecord
from TodoListApp.views import checkExistID

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/', TemplateView.as_view(template_name="todo.html")),
    url(r'^loadTasks/', loadTask, name = "loadTaskURL"),
    url(r'^checkID/', checkExistID , name = "checkIDURL"),
    url(r'^addTask/', addTaskRecord, name = "addDrawingsURL"),
]
