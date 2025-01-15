from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Topic, Post

# Create your views here.
class TopicList(generic.ListView):
    queryset = Topic.objects.all()
    template_name = "feed/index.html"
    paginate_by = 10

posts = [
    {
        'author': 'Tafadzwa testing',
        'title': 'Post 1',
        'content': 'content test',
        'date_posted': '12 January, 2025'
    },
    {
        'author': 'Tafadzwa testing2',
        'title': 'Post 2',
        'content': 'content test2',
        'date_posted': '12 January, 2025'
    }
]

def my_feed(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'feed/index.html', context)