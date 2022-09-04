from django import forms

class DeployForm(forms.Form):
    stack_name = forms.CharField(max_length=15)
    create_yml = forms.CharField(widget=forms.Textarea)
