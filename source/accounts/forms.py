from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username', required=True)
    first_name = forms.CharField(max_length=100, label='First Name', required=False)
    last_name = forms.CharField(max_length=100, label='Second Name', required=False)
    password = forms.CharField(max_length=100, label='Password', required=True,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label='Password Confirm', required=True,
                                       widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('User with this username already exists',
                                  code='user_username_exists')
        except User.DoesNotExist:
            return username

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_confirm']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if password_1 != password_2:
            raise ValidationError('Passwords do not match',
                                  code='passwords_do_not_match')

        if not first_name and not last_name:
            raise ValidationError('First name or Last name must be filled')

        return self.cleaned_data


