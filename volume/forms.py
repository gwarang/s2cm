from django import forms

class CreateForm(forms.Form):
    volume_name = forms.CharField(max_length=15)

class RemoveForm(forms.Form):
    volume_name = forms.CharField(max_length=15)

