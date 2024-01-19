from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from mysite_urls_and_views.department.models import Department


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("It works!")


def department_by_name(request: HttpRequest, department_name: str) -> HttpResponse:
    try:
        department = Department.objects.get(name=department_name)
        context = {"department_name": department.name, "department_id": department.id}
        return render(request, "department/department_details.html", context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("No matching department")


def department_by_id(request: HttpRequest, department_id: int) -> HttpResponse:
    try:
        department = Department.objects.get(id=department_id)
        context = {"department_name": department.name, "department_id": department.id}
        return render(request, "department/department_details.html", context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("No matching department")
