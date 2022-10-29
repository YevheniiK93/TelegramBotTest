from django import forms
from manager.models import UserSubmit
import re


class UserSubmitForm(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        min_length=2,
        widget=forms.TextInput(attrs={
            'type': "text",
            'placeholder': "Name"
        }))

    phone = forms.CharField(
        max_length=15,
        min_length=10,
        widget=forms.TextInput(attrs={
            'type': "text",
            'class': "phone",
            'placeholder': "Phone"
        }))

    message = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={
            'type': "text",
            'placeholder': "Message"
        }))

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(re.findall(r"^[A-Za-zА-Яа-яІіЄєЇї]{2,30}[ A-Za-zА-Яа-яІіЄєЇї]{2,30}?$", data)) == 1:
            return data
        raise forms.ValidationError("Input name correctly")

    def clean_phone(self):
        data = self.cleaned_data["phone"]
        if len(re.findall(r"^(\d{3}[- ]?){2}\d{4,11}$", data)) == 1:
            return data
        raise forms.ValidationError("Input phone number correctly")


    class Meta:
        model = UserSubmit
        fields = ('name', 'phone', 'message')
