# Generated by Django 5.0.4 on 2024-04-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_categoryevent_alter_event_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='url',
            field=models.URLField(default='http://new-team.space'),
            preserve_default=False,
        ),
    ]