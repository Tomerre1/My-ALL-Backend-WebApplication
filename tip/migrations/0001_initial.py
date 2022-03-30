# Generated by Django 3.2 on 2022-03-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.TextField(max_length=100, primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.CharField(max_length=100)),
                ('label', models.JSONField(blank=True, default=list, null=True)),
            ],
        ),
    ]
