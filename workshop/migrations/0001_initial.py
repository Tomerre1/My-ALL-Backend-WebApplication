# Generated by Django 3.2 on 2022-03-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.TextField(max_length=100, primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=100)),
                ('content', models.CharField(max_length=1500)),
                ('title', models.CharField(max_length=100)),
                ('lecturer', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('isDone', models.BooleanField(default=False)),
            ],
        ),
    ]
