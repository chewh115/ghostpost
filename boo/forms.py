from django import forms

class BoastOrRoastForm(forms.Form):
    BOAST_OR_ROAST = [(True, 'Boast'), (False, 'Roast')]
    title = forms.CharField(max_length=30)
    post = forms.CharField(max_length=280)
    boast_or_roast = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=BOAST_OR_ROAST
    )


class SortPosts(forms.Form):
    SORT_CHOICES = [
        ('newest', 'Newest'),
        ('oldest', 'Oldest'),
        ('liked', 'Most liked'),
        ('disliked', 'Least liked')
    ]
    sorting_posts = forms.ChoiceField(
        choices=SORT_CHOICES
    )