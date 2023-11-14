from django.db import models
from django.core.validators import ValidationError, MinValueValidator


def validate_name(value: str):
    for ch in value:
        if not (ch.isalpha() or not ch.isspace()):
            raise ValidationError("Name can only contain letters and spaces")


def validate_phone(value: str):
    if not value.startswith("+359") or not value[4:].isnumeric():
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")


class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, message="Age must be greater than 18")])
    email = models.EmailField(error_messages={"invalid": "Enter a valid email address"})
    phone_number = models.CharField(max_length=13, validators=[validate_phone])
    website_url = models.URLField(error_messages={"invalid": "Enter a valid URL"})
