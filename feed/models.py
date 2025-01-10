from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)


    #class Meta:
    #    ordering = ["-created_on"]


    def __str__(self):
        return f"Topic title: {self.title}"


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="my_feed"
    )
    author = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="my_feed"
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_on"]


    def __str__(self):
        return f"Post title: {self.title}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]


    def __str__(self):
        return f"{self.author} commented {self.body}"


class Report(models.Model):
    REASON_CHOICES = [
        ('SPAM', 'Spam'),
        ('INAP', 'Inappropriate Content'),
        ('HATE', 'Hate Speech'),
        ('OTHER', 'Other'),
    ]

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="reports"
    )
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reports"
    )
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    details = models.TextField(blank=True, null=True, help_text="Additional details about the report (optional)")
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-reported_at"]
        verbose_name_plural = "Reports"

    def __str__(self):
        return f"Report by {self.reporter.username} on {self.post.title}"