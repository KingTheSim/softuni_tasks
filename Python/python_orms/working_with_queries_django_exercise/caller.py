import os
import django
from django.db.models import Case, When, Value, F, Q, QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ready_to_use_django_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop


def show_highest_rated_art() -> str:
    highest = ArtworkGallery.objects.order_by("-rating", "id").first()
    return f"{highest.art_name} is the highest-rated art with a {highest.rating} rating!"


def bulk_create_arts(first_art, second_art) -> None:
    ArtworkGallery.objects.bulk_create((first_art, second_art))


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop() -> str:
    most_expensive = Laptop.objects.order_by("-price", "-id").first()
    return f"{most_expensive.brand} is the most expensive laptop available for {most_expensive.price}$!"


def bulk_create_laptops(*args) -> None:
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems() -> None:
    laptops = Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value("Windows")),
            When(brand="Apple", then=Value("MacOS")),
            When(brand__in=["Dell", "Acer"], then=Value("Linux")),
            When(brand="Lenovo", then=Value("Chrome OS")),
            default=F("OS")
        )
    )


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()
