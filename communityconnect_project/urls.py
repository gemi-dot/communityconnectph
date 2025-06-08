"""
URL configuration for communityconnect_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from orders import views_staff  # ✅ ADD THIS LINE

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('core.urls')),
    path('', include('pages.urls')),  # This will handle the homepage and other pages

    path('orders/', include('orders.urls')),  # 👈 include orders app

    path('staff/dashboard/', views_staff.staff_dashboard, name='staff_dashboard'),  # direct shortcut
    path('staff/request/<int:pk>/update/', views_staff.update_request, name='update_request'),

]


