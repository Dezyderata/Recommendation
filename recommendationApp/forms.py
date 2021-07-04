from django import forms
from django.core import validators
from recommendationApp.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(validators=[validators.MinLengthValidator(3)])
    password = forms.CharField(widget=forms.PasswordInput(),
                               validators=[validators.MinLengthValidator(8)])
    verify_password = forms.CharField(label="Repeat password",
                                      widget=forms.PasswordInput(),
                                      validators=[validators.MinLengthValidator(8)])
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
        'password': forms.PasswordInput(),
        }

    def clean(self):
        all_clean_data = super()
        passwd = all_clean_data.clean().get('password')
        vpasswd = all_clean_data.clean().get('verify_password')
        if passwd != vpasswd:
            raise forms.ValidationError("Passwords doesn't match!")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
        'password': forms.PasswordInput(),
        }



class MovieForm(forms.Form):
    title = forms.CharField(validators=[validators.MinLengthValidator(1)])
    rate = forms.IntegerField(validators=[validators.MaxValueValidator(5),
                                          validators.MinValueValidator(1)])
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
