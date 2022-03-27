# Generated by Django 3.2 on 2022-03-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=100)),
                ('content', models.CharField(max_length=1500)),
                ('title', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=100)),
                ('isDone', models.BooleanField(default=False)),
            ],
        ),
    ]