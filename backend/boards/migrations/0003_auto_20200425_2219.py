# Generated by Django 3.0.4 on 2020-04-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_board_background_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
