# Generated by Django 4.2.17 on 2025-01-27 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_remove_post_report_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='saved_by',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
