from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='report_count',
            field=models.IntegerField(default=0),
        ),
    ]
