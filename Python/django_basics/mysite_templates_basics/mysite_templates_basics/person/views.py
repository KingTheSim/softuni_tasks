import random

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from mysite_templates_basics.person.models import Person
from mysite_templates_basics.person.forms import PersonForm


def person_per_id(request: HttpRequest, person_id: int) -> HttpResponse:
    try:
        person = Person.objects.get(id=person_id)
        context = {
            "full_name": person.full_name,
            "age": person.age,
            "height": person.height,
            "birth_date": person.birth_date,
            "wake_up_time": person.wake_up_time,
            "is_student": person.is_student,
            "email": person.email,
            "website_url": person.website_url,
            "profile_picture": person.profile_picture,
            "document_file": person.document_file,
            "bio": person.bio,
            "test_list_with_nums": [random.randint(1, 100) for _ in range(10)]
        }
        return render(request, template_name="person/person.html", context=context)
    except ObjectDoesNotExist:
        return HttpResponse("Person not found!")


def add_new_person(request: HttpRequest) -> HttpResponse:
    form = PersonForm(request.POST or None)

    if form.is_valid():
        new_person: Person = form.save()
        return redirect("person_per_id", person_id=new_person.id)

    return render(request, "person/person_form.html", {"form": form})


def update_person(request: HttpRequest, person_id: int) -> HttpResponse:
    person = get_object_or_404(Person, id=person_id)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect("person_per_id", person_id=person_id)
    else:
        return render(request, "person/person_update.html", {"form": form})
