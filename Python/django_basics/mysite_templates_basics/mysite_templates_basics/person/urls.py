from django.urls import path
from mysite_templates_basics.person import views

urlpatterns = [
    path("<int:person_id>/", views.person_per_id, name="person_per_id"),
]