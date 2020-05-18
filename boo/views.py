from django.shortcuts import render, reverse, HttpResponseRedirect
from boo.models import BoastAndRoast
from boo.forms import BoastOrRoastForm, SortPosts

# This answer REALLY helped me work through the booleanfield + its use in views:
# https://stackoverflow.com/questions/29714763/django-check-if-checkbox-is-selected

# Create your views here.
def index(request):
    context = {}
    posts =  BoastAndRoast.objects.all()
    context['posts'] = posts
    context['form'] = SortPosts()
    if 'boasts' in request.path:
        context['posts'] = posts.filter(boast_or_roast=True)
    if 'roasts' in request.path:
        context['posts'] = posts.filter(boast_or_roast=False)
    if request.method == 'POST':
        form = SortPosts(request.POST)
        if form.is_valid():
            sort_method = form.cleaned_data.get('sorting_posts')
            if sort_method == 'newest':
                context['posts'] = posts.order_by('-submit_time')
            elif sort_method == 'oldest':
                context['posts'] = posts.order_by('submit_time')
            elif sort_method == 'liked':
                posts = sorted(posts, key=lambda x: -x.score())
                context['posts'] = posts
            elif sort_method == 'disliked':
                posts = sorted(posts, key=lambda x: x.score())
                context['posts'] = posts
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


def up_vote(request, post_id):
    post = BoastAndRoast.objects.get(id=post_id)
    post.up_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def down_vote(request, post_id):
    post = BoastAndRoast.objects.get(id=post_id)
    post.down_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))