import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


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


def delete_last_car() -> None:
    Car.objects.last().delete()


def show_unfinished_tasks() -> str:
    unfinished = Task.objects.filter(is_finished=False)
    unfinished = [str(task) for task in unfinished]
    return "\n".join(unfinished)


def complete_odd_tasks() -> None:
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str) -> None:
    encoded_text = "".join(chr(ord(t) - 3) for t in text)

    tasks = Task.objects.filter(title=task_title)
    for task in tasks:
        task.description = encoded_text
        task.save()


def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    deluxe_rooms = [str(room) for room in deluxe_rooms if room.id % 2 == 0]
    return "\n".join(deluxe_rooms)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by("id")

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room() -> None:
    first = HotelRoom.objects.first()
    first.is_reserved = True
    first.save()


def delete_last_room() -> None:
    last = HotelRoom.objects.last()
    if last.is_reserved:
        last.delete()
