# Generated by Django 5.1 on 2024-12-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_validated',
            field=models.BooleanField(default=False),
        ),
    ]
