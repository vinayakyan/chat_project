"""
URL configuration for chat_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from chat_app import views as chat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', LoginView.as_view(template_name="chat_app/login_page.html"), name="login"),
    path('auth/logout/', LogoutView.as_view(), name="logout"),
    path('', chat_views.chat_page, name="chat-page"),
]
