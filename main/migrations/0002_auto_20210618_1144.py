# Generated by Django 3.0.7 on 2021-06-18 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_studentprofile_year_semester'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='dept',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Dept'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.CreateModel(
            name='SemesterDeptSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Dept')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Semester')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Subject')),
            ],
        ),
    ]
