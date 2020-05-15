from django import forms


class BoastOrRoastForm(forms.Form):
    boast_or_roast = forms.BooleanField(widget=forms.CheckboxInput)
    post = forms.CharField(max_length=280)