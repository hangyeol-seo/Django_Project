# Generated by Django 3.0.7 on 2020-06-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personality_text', models.CharField(max_length=10)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
