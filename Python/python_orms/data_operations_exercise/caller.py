import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task


def create_pet(name: str, species: str) -> str:
    Pet.objects.create(name=name, species=species)
    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    Artifact.objects.create(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


def show_all_locations() -> str:
    locations = Location.objects.all().order_by("-id")
    new_locations = [f"{loc.name} has a population of {loc.population}!" for loc in locations]
    return "\n".join(new_locations)


def new_capital() -> None:
    cap = Location.objects.first()
    cap.is_capital = True
    cap.save()


def get_capitals():
    return Location.objects.all().filter(is_capital=True).values("name")


def delete_first_location() -> None:
    Location.objects.first().delete()


def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        percentage_off = sum(int(x) for x in str(car.year)) / 100
        discount = float(car.price) * percentage_off
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values("model", "price_with_discount")


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_task() -> str:
    unfinished = Task.objects.filter(is_finished=False).values("title", "due_date")
    unfinished = [f"Task - {task.title} needs to be done until {task.due_date}!" for task in unfinished]
    return f"\n".join(unfinished)


def complete_odd_tasks():
    odds = Task.objects.filter(id__mod=1, is_finished=False)
    odds.update(is_finished=True)