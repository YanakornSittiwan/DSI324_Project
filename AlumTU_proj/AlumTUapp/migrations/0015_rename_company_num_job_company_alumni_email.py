# Generated by Django 4.0.3 on 2022-04-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumTUapp', '0014_alter_job_consent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='Company_num',
            new_name='Company',
        ),
        migrations.AddField(
            model_name='alumni',
            name='Email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
