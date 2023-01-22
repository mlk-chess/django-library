from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    roles = (
        ('client_role', 'Client'),
        ('bookseller_role', 'Bookseller')
    )

    inputClass = "form-control";

    username = forms.CharField(max_length=63, label='Username', widget=forms.TextInput(
        attrs={'class': inputClass, 'placeholder' : 'ESGI'}
    ))
    email = forms.EmailField(max_length=254, label='email', widget=forms.EmailInput(
        attrs={'class': inputClass, 'placeholder' : 'name@example.com'}
    ))
    address = forms.CharField(max_length=254, label='email', widget=forms.TextInput(
        attrs={'class': inputClass, 'placeholder' : '252 rue Faubourg Saint Antoine'}
    ))
    first_name = forms.CharField(max_length=63, label='firstname', widget=forms.TextInput(
        attrs={'class': inputClass, 'placeholder' : 'Sensui'}
    ))
    last_name = forms.CharField(max_length=63, label='lastname', widget=forms.TextInput(
        attrs={'class': inputClass, 'placeholder' : 'Shinobu'}
    ))
    role = forms.ChoiceField(choices=roles, label='Role', widget=forms.Select(
        attrs={'class': inputClass}
    ))
    password1 = forms.CharField(max_length=63, label='Password', widget=forms.PasswordInput(
        attrs={'class': inputClass, 'placeholder' : 'password'}
    ))
    password2 = forms.CharField(max_length=63, label='Confirmation password', widget=forms.PasswordInput(
        attrs={'class': inputClass, 'placeholder' : 'Confirm password'}
    ))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')
