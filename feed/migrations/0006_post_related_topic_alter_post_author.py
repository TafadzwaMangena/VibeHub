from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0005_post_dislikes_post_likes_post_saved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='related_topic',
            field=models.ForeignKey(
                default='1',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='my_feed',
                to='feed.topic'
                ),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='my_feed',
                to=settings.AUTH_USER_MODEL
                ),
        ),
    ]
