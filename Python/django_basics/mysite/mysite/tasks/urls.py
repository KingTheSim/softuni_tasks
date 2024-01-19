from django.urls import path

from mysite.tasks.views import index

urlpatterns = [
    path('', index)
]
