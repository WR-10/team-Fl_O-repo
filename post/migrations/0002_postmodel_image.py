# Generated by Django 4.1.1 on 2022-10-03 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='image',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
