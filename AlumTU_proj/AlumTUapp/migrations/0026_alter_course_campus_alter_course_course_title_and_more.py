# Generated by Django 4.0.4 on 2022-05-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumTUapp', '0025_alter_job_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Campus',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='Course_title',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='course',
            name='Faculty',
            field=models.CharField(max_length=70),
        ),
    ]
