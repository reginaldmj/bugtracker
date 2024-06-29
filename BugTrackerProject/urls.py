"""BugTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from BugTrackerApp import views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('bug/<int:id>/', views.bug, name='bug'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_action, name='logout'),
    path('addbug/', views.add_bug, name='addbug'),
    path('editbug/<int:id>/', views.edit_bug, name='editbug'),
    path('user/<int:id>/', views.user, name='user'),
    path('assignticket/<int:id>/', views.assignticket, name='assignticket'),
    path('assigncomplete/<int:id>/', views.assigncomplete, name='assigncomplete'),
    path('assigninvalid/<int:id>/', views.assigninvalid, name='assigninvalid'),

]
