from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_topic_excerpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
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
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                (
                    'status',
                    models.IntegerField(
                        choices=[(0, 'Draft'), (1, 'Published')], default=0
                        )
                        ),
                (
                    'excerpt',
                    models.TextField(blank=True)
                ),
                ('updated_on', models.DateTimeField(auto_now=True)),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='my_feed',
                        to='feed.topic'
                        )
                        ),
            ],
        ),
    ]
