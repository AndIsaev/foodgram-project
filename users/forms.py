from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CreationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Илон"}),
    )
    username = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Mask"}),
    )
    email = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "tesla@mars.com"}),
    )

    class Meta:
        model = User
        fields = ("first_name", "username", "email")
