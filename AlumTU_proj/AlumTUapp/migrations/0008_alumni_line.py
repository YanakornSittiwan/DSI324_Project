# Generated by Django 4.0.3 on 2022-04-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumTUapp', '0007_alumni_name_alumni_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='Line',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
