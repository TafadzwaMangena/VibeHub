from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_post_related_topic_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
