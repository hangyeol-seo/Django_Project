# Generated by Django 3.0.7 on 2020-06-14 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compare', '0006_auto_20200609_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageuploadmodel',
            name='uploader',
            field=models.ForeignKey(default='shy73', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
