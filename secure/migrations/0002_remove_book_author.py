# Generated by Django 4.1.3 on 2022-11-13 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]
