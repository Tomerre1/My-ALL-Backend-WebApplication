# Generated by Django 3.2 on 2022-05-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.TextField(max_length=100, primary_key=True, serialize=False)),
                ('mailUser', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('mail', models.EmailField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('img', models.URLField(max_length=1500)),
            ],
        ),
    ]
