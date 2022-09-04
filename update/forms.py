from django import forms

class UpdateForm(forms.Form):
    update_image_name = forms.CharField(max_length=100)

