# Generated by Django 3.0.7 on 2021-06-18 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20210618_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewdetails',
            name='revpoint',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
