from django import forms
from django.core.validators import EmailValidator


class LoginForm(forms.Form):
    UserName = forms.CharField(max_length = 15, label= 'UserName', widget = forms.TextInput(
        attrs = {
            'class' : "form-control",
            'placeholder' : "UserName",
            "id" : "exampleInputEmail1"
            }
        ))
    password = forms.CharField(max_length=15, widget = forms.PasswordInput(
        attrs = {
            "class" : "form-control",
            "type" : "password",
            "id" : "exampleInputPassword1",
            "placeholder" : "Password"
        }
    ))

class CreateUser(forms.Form):
    FirstName = forms.CharField(max_length = 15, label= 'First Name', widget = forms.TextInput(
        attrs = {
            'class' : "form-control",
            'placeholder' : "First Name",
            "id" : "exampleInputEmail1"
            }
        ))
    LastName = forms.CharField(max_length = 15, label= 'Last Name', widget = forms.TextInput(
        attrs = {
            'class' : "form-control",
            'placeholder' : "Last Name",
            "id" : "exampleInputEmail1"
            }
        ))
    UserName = forms.CharField(max_length = 15, label= 'UserName', widget = forms.TextInput(
        attrs = {
            'class' : "form-control",
            'placeholder' : "UserName",
            "id" : "exampleInputEmail1"
            }
        ))
    Email = forms.CharField(max_length = 30, label= 'Email Id', validators = [EmailValidator], widget = forms.TextInput(
    attrs = {
        'class' : "form-control",
        'placeholder' : "Email",
        "id" : "exampleInputEmail1"
        }
    ))
    password = forms.CharField(max_length=15, widget = forms.PasswordInput(
    attrs = {
        "class" : "form-control",
        "type" : "password",
        "id" : "exampleInputPassword1",
        "placeholder" : "Password"
    }
))