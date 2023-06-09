# Generated by Django 3.2.5 on 2021-11-12 06:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slung', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('founded', models.CharField(max_length=100)),
                ('stadium', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Team',
            },
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 8, 3, 47, 343744), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slung.team')),
            ],
            options={
                'verbose_name_plural': 'Player',
            },
        ),
    ]
