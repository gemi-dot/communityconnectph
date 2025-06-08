from django.urls import path
from . import views
from . import views_staff


urlpatterns = [
    path('water-order/', views.water_order_request, name='water_order'),

    path('staff/dashboard/', views_staff.staff_dashboard, name='staff_dashboard'),
    path('staff/request/<int:pk>/update/', views_staff.update_request, name='update_request'),



]
