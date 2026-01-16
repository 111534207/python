"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# my_project/urls.py
from django.contrib import admin
from django.urls import path, include  # 記得要匯入 include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 👇 這一行就是解決 logout 錯誤的關鍵！它包含了 login 和 logout 的路徑
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 連接到 core 應用程式
    path('', include('core.urls')),
]
