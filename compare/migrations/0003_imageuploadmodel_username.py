# Generated by Django 3.0.7 on 2020-06-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0002_auto_20200608_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageuploadmodel',
            name='username',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
