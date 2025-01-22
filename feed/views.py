from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
import datetime
from django.utils import timezone
from .models import Topic, Post, Report
from .forms import PostForm


def my_feed(request):
    topics = Topic.objects.all()
    posts = Post.objects.all().order_by('-created_on') # Fetch all posts, ordered by most recent

    context = {
        'topics': topics,
        'posts': posts,
    }

    return render(request, 'feed/index.html', context)


# Create a post
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign the logged-in user as the author
            post.save()
            return redirect("feed")
    else:
        form = PostForm()
    return render(request, "feed/post_create.html", {"form": form})


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