# Generated by Django 4.0.3 on 2022-04-14 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumTUapp', '0003_alumni_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='PhoneNumber',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
