# Generated by Django 3.0.6 on 2020-05-10 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0004_showrates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shows',
            name='users_rating',
        ),
    ]
