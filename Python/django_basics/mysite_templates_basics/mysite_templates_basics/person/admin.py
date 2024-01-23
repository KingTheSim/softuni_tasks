from django.contrib import admin
from mysite_templates_basics.person.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
