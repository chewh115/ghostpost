from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Found the MinValueValidator from both Django's documentation and this post:
# https://www.reddit.com/r/django/comments/2q5u0p/way_to_make_a_min_and_max_values_restriction_on_a/

# Boolean to tell whether it's a boast or a roast - DONE, null is value
# and checkboxInput on form will check true or false


# Create your models here.
class BoastAndRoast(models.Model):
    boast_or_roast = models.BooleanField()
    title = models.CharField(max_length=30)
    post = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0, editable=False, validators=[MinValueValidator(0)])
    down_votes = models.IntegerField(default=0, editable=False, validators=[MinValueValidator(0)])
    submit_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
