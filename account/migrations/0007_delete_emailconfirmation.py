# Generated by Django 3.0.7 on 2021-07-06 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_emailconfirmation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailConfirmation',
        ),
    ]
