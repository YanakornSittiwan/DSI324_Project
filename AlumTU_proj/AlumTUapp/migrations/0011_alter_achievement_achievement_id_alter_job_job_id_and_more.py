# Generated by Django 4.0.3 on 2022-04-28 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumTUapp', '0010_alter_alumni_linkedin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='Achievement_id',
            field=models.IntegerField(auto_created=True, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='Job_id',
            field=models.IntegerField(auto_created=True, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]