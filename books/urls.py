"""books URL Configuration

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
from mainapp.views import main_page, page_in_process
from authnapp.views import login_page, registration_page, logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_page, name='copleated_book'),
    path("process/", page_in_process, name='process_books'),
    path('login/', login_page, name='login'),
    path('logout/', logout, name='logout'),
    path('reg/', registration_page, name='reg')
]
