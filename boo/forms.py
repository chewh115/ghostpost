from django import forms

class BoastOrRoastForm(forms.Form):
    BOAST_OR_ROAST = ((True, 'Boast'), (False, 'Roast'))
    boast_or_roast = forms.ChoiceField(
        label='Boast or Roast?',
        widget=forms.RadioSelect,
        choices=BOAST_OR_ROAST
    )
    title = forms.CharField(max_length=30)
    post = forms.CharField(max_length=280)
