from django import forms

class LoginForm(forms.Form):
    docker_id = forms.CharField()
    docker_pw = forms.CharField()
