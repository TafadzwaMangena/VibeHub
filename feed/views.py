from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
import datetime
from django.utils import timezone
from .models import Topic, Post, Report

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


def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('feed')
    return render(request, 'feed/post_create.html')


# Create a post
@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('feed')
    return render(request, 'feed/post_create.html')

# Update a post
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('feed')
    return render(request, 'feed/post_update.html', {'post': post})

# Delete a post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('feed')

# Report a post
@login_required
def report_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        reason = request.POST['reason']
        details = request.POST.get('details', '')
        Report.objects.create(
            post=post, reporter=request.user, reason=reason, details=details
        )
        return JsonResponse({'success': True, 'total_reports': post.reports.count()})
    return render(request, 'feed/report_post.html', {'post': post})