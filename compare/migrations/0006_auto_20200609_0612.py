# Generated by Django 3.0.7 on 2020-06-08 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0005_imageuploadmodel_blog_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageuploadmodel',
            name='best_character',
            field=models.CharField(default='None', max_length=10),
        ),
        migrations.AddField(
            model_name='imageuploadmodel',
            name='sim',
            field=models.IntegerField(default=0),
        ),
    ]