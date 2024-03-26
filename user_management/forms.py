from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.add_input(
            Submit("register-submit","Submit",css_class="rounded-pill btn mt-4")
        )

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User already exist!")
        return email



class LoginForm(AuthenticationForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.add_input(
            Submit("login-submit","Login",css_class="rounded-pill btn mt-4")
        )
