from django.contrib import admin
from mysite_urls_and_views.department.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
