# Generated by Django 2.2.7 on 2022-02-08 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_delete_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='pass_updated',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]