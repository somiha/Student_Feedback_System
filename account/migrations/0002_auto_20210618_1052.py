# Generated by Django 3.0.7 on 2021-06-18 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='year_semester',
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='batch',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Batch'),
        ),
    ]