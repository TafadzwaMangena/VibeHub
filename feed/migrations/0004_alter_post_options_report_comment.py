from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0003_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                        )
                        ),
                (
                    'reason',
                    models.CharField(
                        choices=[
                            ('SPAM', 'Spam'),
                            ('INAP', 'Inappropriate Content'),
                            ('HATE', 'Hate Speech'),
                            ('OTHER', 'Other')
                            ],
                        max_length=20
                            )
                            ),
                (
                    'details',
                    models.TextField(
                        blank=True,
                        help_text='Additional details about the report (optional)',
                        null=True
                        )
                        ),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                (
                    'post',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reports',
                        to='feed.post'
                        )
                        ),
                (
                    'reporter',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reports',
                        to=settings.AUTH_USER_MODEL
                        )
                        ),
            ],
            options={
                'verbose_name_plural': 'Reports',
                'ordering': ['-reported_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                        )
                        ),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='commenter',
                        to=settings.AUTH_USER_MODEL
                        )
                        ),
                (
                    'post',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        to='feed.post'
                        )
                        ),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
