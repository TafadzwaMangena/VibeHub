from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
