"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, TaskCreateView, TaskView, TaskUpdateView, TaskDeleteView, StatusIndexView, \
    StatusCreateView, StatusUpdateView, StatusDeleteView, TypeIndexView, TypeCreateView, TypeUpdateView, \
    TypeDeleteView, ProjectIndexView, ProjectView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('issue/add/', TaskCreateView.as_view(), name="task_add"),
    path('issue/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('issue/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('status', StatusIndexView.as_view(), name='status'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('status/<int:pk>/update', StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete', StatusDeleteView.as_view(), name='status_delete'),
    path('type', TypeIndexView.as_view(), name='type'),
    path('type/add/', TypeCreateView.as_view(), name='type_add'),
    path('type/<int:pk>/update/', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete', TypeDeleteView.as_view(), name='type_delete'),
    path('project', ProjectIndexView.as_view(), name='project'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete')

]