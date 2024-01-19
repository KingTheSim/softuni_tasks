from django.urls import path

from mysite_urls_and_views.department import views

urlpatterns = [
    path('', views.index),
    path('<int:department_id>/', views.department_by_id),
    path('<str:department_name>/', views.department_by_name),
]