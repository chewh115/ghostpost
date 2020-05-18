from django.shortcuts import render, reverse, HttpResponseRedirect
from boo.models import BoastAndRoast
from boo.forms import BoastOrRoastForm, SortPosts

# This answer REALLY helped me work through the booleanfield + its use in views:
# https://stackoverflow.com/questions/29714763/django-check-if-checkbox-is-selected

# Create your views here.
def index(request):
    context = {}
    context['posts'] = BoastAndRoast.objects.all()
    context['form'] = SortPosts()
    if request.method == 'POST':
        form = SortPosts(request.POST)
        if form.is_valid():
            sort_method = form.cleaned_data.get('sorting_posts')
            if sort_method == 'newest':
                context['posts'] = BoastAndRoast.objects.all().order_by('-submit_time')
            elif sort_method == 'oldest':
                context['posts'] = BoastAndRoast.objects.all().order_by('submit_time')
            return render(request, 'index.html', context)
            
    return render(request, 'index.html', context)


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