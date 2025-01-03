# Generated by Django 5.1.4 on 2025-01-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_is_validated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
