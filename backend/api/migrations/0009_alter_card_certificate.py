# Generated by Django 5.0.4 on 2024-04-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_hospital_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='certificate',
            field=models.ImageField(null=True, upload_to='certificates/'),
        ),
    ]
