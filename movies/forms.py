from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from movies.models import User


class NewUserForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"type": "username", "placeholder": ("Username")})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "first_name", "placeholder": ("First Name")}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "last_name", "placeholder": ("Last Name")}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"type": "email", "placeholder": ("Email")})
    )
    password1 = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(
            attrs={
                # 'class':'form-control',
                "placeholder": "Password"
            }
        ),
    )
    password2 = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(
            attrs={
                # 'class':'form-control',
                "placeholder": "Repeat Password"
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class MovieSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..."}),
    )
