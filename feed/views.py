from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Topic, Post

# Create your views here.
# class TopicList(generic.ListView):
#     queryset = Topic.objects.all()
#     template_name = "feed/index.html"
#     paginate_by = 10

#     def my_feed(request):
#     context = {
#         'posts': Post.objects.all
#     }
#     return render(request, 'feed/index.html', context)

def my_feed(request):
    topics = Topic.objects.all()
    posts = Post.objects.all()

    context = {
        'topics': topics,
        'posts': posts,
    }

    return render(request, 'feed/index.html', context)