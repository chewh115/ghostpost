from django.shortcuts import render, reverse, HttpResponseRedirect
from boo.models import BoastAndRoast
from boo.forms import BoastOrRoastForm

# This answer REALLY helped me work through the booleanfield + its use in views:
# https://stackoverflow.com/questions/29714763/django-check-if-checkbox-is-selected

# Create your views here.
def index(request):
    posts = BoastAndRoast.objects.all().order_by('submit_time')
    return render(request, 'index.html')


def submit(request):
    if request.method == "POST":
        form = BoastOrRoastForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastAndRoast.objects.create(
                boast_or_roast=data['boast_or_roast'],
                title=data['title'],
                post=data['post'],
                up_votes=0,
                down_votes=0
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = BoastOrRoastForm()
    return render(request, 'submit.html', {'form': form})