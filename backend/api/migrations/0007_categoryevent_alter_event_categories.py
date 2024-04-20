# Generated by Django 5.0.4 on 2024-04-20 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_card_for_kid_delete_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='categories',
        ),
        migrations.AddField(
            model_name='event',
            name='categories',
            field=models.ManyToManyField(related_name='events', through='api.CategoryEvent', to='api.category'),
        )
    ]
