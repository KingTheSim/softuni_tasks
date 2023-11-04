import os
from datetime import timedelta, date
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Avg
from main_app.models import (Author, Book, Artist, Song, Product, Review,
                             Driver, DrivingLicense, Owner, Car, Registration)


def show_all_authors_with_their_books():
    authors_with_books = []

    all_authors = Author.objects.all().order_by("id")
    for author in all_authors:
        books = author.book_set.all()
        if books:
            books = ", ".join(book.title for book in books)
            authors_with_books.append(f"{author.name} has written - {books}!")

    return "\n".join(authors_with_books)


def delete_all_authors_without_books():
    authors_without_books = []

    all_authors = Author.objects.all()
    for author in all_authors:
        if not author.book_set.exists():
            authors_without_books.append(author)

    for a in authors_without_books:
        a.delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by("-id")


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    artist.songs.remove(Song.objects.get(title=song_title))


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    return Review.objects.filter(product=product).aggregate(Avg("rating"))["rating__avg"]


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.all().order_by("-license_number")
    result = []

    for lic in licenses:
        exp_time = lic.issue_date + timedelta(days=365)
        exp_time = exp_time.strftime("%Y-%m-%d")
        result.append(f"License with id: {lic.license_number} expires on {exp_time}!")

    return "\n".join(result)


def get_drivers_with_expired_licenses(due_date):
    exp_time = due_date - timedelta(days=365)
    return Driver.objects.filter(drivinglicense__issue_date__gte=exp_time)


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(owner=owner).first()

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return (f"Successfully registered {car.model} to {owner.name} "
            f"with registration number {registration.registration_number}.")
