from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_post_report_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='report_count',
        ),
    ]
