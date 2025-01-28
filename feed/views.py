from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
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
            messages.success(request, 'Your post has been created successfully!')
            return redirect("feed")
    else:
        form = PostForm()
    return render(request, "feed/post_create.html", {"form": form})


# Update a post
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    topics = Topic.objects.all()  
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated successfully!')
            return redirect('feed')
    else:
        form = PostForm(instance=post)
    return render(request, 'feed/post_update.html', {'form': form, 'post': post, 'topics': topics})

# Delete a post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'The post has been deleted successfully.')
    return redirect('feed')

# Report a post
@login_required
def report_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        reason = request.POST.get('reason')
        details = request.POST.get('details', '')

        # Save the report
        Report.objects.create(
            post=post, reporter=request.user, reason=reason, details=details
        )

        messages.success(request, f'Thank you for reporting the post: "{post.title}".')

        # Redirect to the feed after report made
        return redirect('feed')
    return render(request, 'feed/report_post.html', {'post': post})


def topic_posts(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = Post.objects.filter(related_topic=topic)
    return render(request, 'feed/topic_posts.html', {'topic': topic, 'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'feed/post_detail.html', {'post': post})


def msg_view(request):
    if request.user.is_authenticated:
        messages.success(request, f"You are logged in as {request.user.username}.")
    else:
        messages.warning(request, "You are not logged in.")