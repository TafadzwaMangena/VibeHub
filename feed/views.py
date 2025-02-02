from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse # noqa
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone # noqa
from .models import Topic, Post, Report
from .forms import PostForm


def my_feed(request):
    """
    Display the main feed with a list of posts, ordered by creation date.
    Includes pagination to limit the number of posts displayed per page.
    """
    topics = Topic.objects.all()
    posts_queryset = Post.objects.all().order_by('-created_on')
    paginator = Paginator(posts_queryset, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(
        request,
        'feed/index.html',
        {
            'topics': topics,
            'posts': posts
        }
    )


@login_required
def post_create(request):
    """
    Allow authenticated users to create a new post.
    If the request method is POST, validate and save the form.
    Otherwise, display an empty form.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(
                request,
                'Your post has been created successfully!'
                )
            return redirect("feed")
    else:
        form = PostForm()
    return render(request, "feed/post_create.html", {"form": form})


@login_required
def post_update(request, pk):
    """
    Allow the post author to update an existing post.
    If the request method is POST, update the post with new data.
    Otherwise, display the form pre-filled with the current post details.
    """
    post = get_object_or_404(Post, pk=pk)
    topics = Topic.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your post has been updated successfully!'
                )
            return redirect('feed')
    else:
        form = PostForm(instance=post)
    return render(
        request,
        'feed/post_update.html',
        {'form': form, 'post': post, 'topics': topics}
    )


@login_required
def post_delete(request, pk):
    """
    Allow the post author to delete their post.
    Once deleted, redirect back to the main feed.
    """
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'The post has been deleted successfully.')
    return redirect('feed')


@login_required
def report_post(request, pk):
    """
    Allow users to report a post for violating community guidelines.
    The report includes a reason and optional details.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        reason = request.POST.get('reason')
        details = request.POST.get('details', '')
        Report.objects.create(
            post=post,
            reporter=request.user,
            reason=reason,
            details=details
            )
        messages.success(
            request,
            f'Thank you for reporting the post: "{post.title}".'
        )
        return redirect('feed')
    return render(request, 'feed/report_post.html', {'post': post})


def topic_posts(request, topic_id):

    """
    Display all posts related to a specific topic.
    """
    topic = get_object_or_404(Topic, id=topic_id)
    posts = Post.objects.filter(related_topic=topic)
    return render(
        request,
        'feed/topic_posts.html', {'topic': topic, 'posts': posts}
    )


def post_detail(request, post_id):
    """
    Show the details of a specific post.
    """
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'feed/post_detail.html', {'post': post})
