from django.urls import path
from mysite_templates_basics.person import views

urlpatterns = [
    path("<int:person_id>/", views.person_per_id, name="person_per_id"),
    path("person_form/", views.add_new_person, name="person_form"),
    path("person_update/<int:person_id>/", views.update_person, name="person_update"),
]
