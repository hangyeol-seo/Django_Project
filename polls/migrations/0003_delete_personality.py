# Generated by Django 3.0.7 on 2020-06-07 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_personality'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Personality',
        ),
    ]
