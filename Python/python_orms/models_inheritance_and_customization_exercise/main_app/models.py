from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator

from datetime import timedelta


class BaseCharacter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True


class Mage(BaseCharacter):
    elemental_power = models.CharField(max_length=100)
    spellbook_type = models.CharField(max_length=100)


class Assassin(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    assassination_technique = models.CharField(max_length=100)


class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    demon_slaying_ability = models.CharField(max_length=100)


class TimeMage(Mage):
    time_magic_mastery = models.CharField(max_length=100)
    temporal_shift_ability = models.CharField(max_length=100)


class Necromancer(Mage):
    raise_dead_ability = models.CharField(max_length=100)


class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(max_length=100)
    venomous_bite_ability = models.CharField(max_length=100)


class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(max_length=100)


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(max_length=100)
    retribution_ability = models.CharField(max_length=100)


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(max_length=100)


class UserProfile(models.Model):
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)


class Message(models.Model):
    sender = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self) -> None:
        self.is_read = True

    def mark_as_unread(self) -> None:
        self.is_read = False

    def reply_to_message(self, reply_content: str, receiver: UserProfile):
        return Message(sender=self.receiver, receiver=receiver, content=reply_content)

    def forward_message(self, sender: UserProfile, receiver: UserProfile):
        return Message(sender=sender, receiver=receiver, content=self.content)


class StudentIDField(models.PositiveIntegerField):
    def to_python(self, value):
        try:
            return int(value)
        except ValueError:
            pass


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = StudentIDField()


class MaskedCreditCardField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 20
        super().__init__(*args, **kwargs)

    def to_python(self, value: str):
        if not isinstance(value, str):
            raise ValidationError("The card number must be a string")

        elif not value.isdigit():
            raise ValidationError("The card number must contain only digits")

        elif len(value) != 16:
            raise ValidationError("The card number must be exactly 16 characters long")

        else:
            return f"****-****-****-{value[-4:]}"


class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField()


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class Room(models.Model):
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE)
    number = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()
    total_guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.total_guests > self.capacity:
            raise ValidationError("Total guests are more than the capacity of the room")

    def save(self, *args, **kwargs):
        self.clean()

        super().save(*args, **kwargs)
        return f"Room {self.number} created successfully"


class BaseReservation(models.Model):
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def reservation_period(self) -> int:
        return (self.end_date - self.start_date).days

    def calculate_total_cost(self) -> float:
        return round((self.reservation_period() * self.room.price_per_night), 1)

    @property
    def available(self) -> bool:
        overlaps = self.__class__.objects.filter(
                                                 room=self.room,
                                                 end_date__gte=self.start_date,
                                                 start_date__lte=self.end_date,
        )

        return not overlaps.exists()

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date cannot be after or in the same end date")

        elif not self.available:
            raise ValidationError(f"Room {self.room.number} cannot be reserved")

    class Meta:
        abstract = True


class RegularReservation(BaseReservation):
    def save(self, *args, **kwargs) -> str:
        super().clean()

        super().save(*args, **kwargs)

        return f"Regular reservation for room {self.room.number}"


class SpecialReservation(BaseReservation):
    def extend_reservation(self, days: int):
        cur_available = SpecialReservation.objects.filter(
            room=self.room,
            end_date__gte=self.start_date,
            start_date__lte=self.end_date + timedelta(days=days),
        )

        if cur_available:
            raise ValidationError("Error during extending reservation")

        else:
            self.end_date += timedelta(days=days)
            self.save()

            return f"Extended reservation for room {self.room.number} with {days} days"

    def save(self, *args, **kwargs):
        super().clean()

        super().save(*args, **kwargs)

        return f"Special reservation for room {self.room.number}"
