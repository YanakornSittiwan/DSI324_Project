# Generated by Django 4.0.3 on 2022-04-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumTUapp', '0012_alter_alumni_address_alter_alumni_line_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Consent',
            field=models.CharField(default='yes', max_length=3),
        ),
    ]
