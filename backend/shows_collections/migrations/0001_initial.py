# Generated by Django 3.1.2 on 2020-11-07 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shows_collections.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('show', '0008_auto_20200928_1910'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Board',
                'db_table': 'shows_collections',
            },
            bases=(models.Model, ),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_outside_board', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Shows list',
                'db_table': 'shows_list',
            },
            bases=(models.Model, ),
        ),
        migrations.CreateModel(
            name='ListShowRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows_collections.list')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.shows')),
            ],
            options={
                'verbose_name': 'List show',
                'db_table': 'list_show_relations',
            },
        ),
        migrations.CreateModel(
            name='BoardMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows_collections.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Board member',
                'db_table': 'board_members',
            },
        ),
        migrations.CreateModel(
            name='BoardLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows_collections.board')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows_collections.list')),
            ],
            options={
                'verbose_name': 'Board list',
                'db_table': 'board_lists',
            },
        ),
        migrations.CreateModel(
            name='BoardFollowers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False, null=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows_collections.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Board follower',
                'db_table': 'board_followers',
            },
        ),
    ]
