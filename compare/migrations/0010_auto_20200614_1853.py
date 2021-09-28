# Generated by Django 3.0.7 on 2020-06-14 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compare', '0009_auto_20200614_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageuploadmodel',
            name='uploader',
        ),
        migrations.AddField(
            model_name='imageuploadmodel',
            name='uploader_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
