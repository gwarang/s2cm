from django import forms

class CreateForm(forms.Form):
    network_name = forms.CharField(max_length=15)
    CHOICES = [('overlay', 'overlay'), ('bridge', 'bridge')]
    driver = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    attachable = forms.BooleanField(required=False)

class RemoveForm(forms.Form):
    network_name = forms.CharField(max_length=15)

