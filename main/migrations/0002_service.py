# Generated by Django 4.1.5 on 2023-01-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(default='Not service available yet', max_length=50)),
                ('service_price', models.CharField(default='Not service available yet', max_length=50)),
                ('options', models.TextField(default='Not service available yet')),
            ],
        ),
    ]