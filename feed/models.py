from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


STATUS = ((0, "Draft"), (1, "Published"))


class Topic(models.Model):
    """
    Represents a discussion topic that posts can be categorized under.
    """
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

    def __str__(self):
        """
        Returns a string representation of the topic.
        """
        return f"Topic title: {self.title}"


class Post(models.Model):
    """
    Represents a post created by a user, which belongs to a specific topic.
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="my_feed"
    )
    related_topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="my_feed",
        default="1"
    )
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def is_updated(self):
        """
        Checks if the post has been updated by comparing the creation
        and last updated timestamps.
        """
        return self.updated_on - self.created_on > timedelta(seconds=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string representation of the post.
        """
        return f"Post title: {self.title}"


class Report(models.Model):
    """
    Represents a report submitted by a user regarding a post,
    providing a reason and optional details.
    """
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
    details = models.TextField(
        blank=True, null=True,
        help_text="Additional details about the report (optional)"
    )
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-reported_at"]
        verbose_name_plural = "Reports"

    def __str__(self):
        """
        Returns a string representation of the report.
        """
        return f"Report by {self.reporter.username} on {self.post.title}"
