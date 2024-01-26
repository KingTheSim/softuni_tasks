from django import forms
from mysite_templates_basics.person.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        labels = {
            "full_name": "Person's Full Name"
        }
        help_texts = {
            "email": "Enter a valid email here!"
        }
