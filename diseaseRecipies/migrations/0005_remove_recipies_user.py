# Generated by Django 3.2.7 on 2021-09-28 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseaseRecipies', '0004_auto_20210929_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipies',
            name='user',
        ),
    ]
