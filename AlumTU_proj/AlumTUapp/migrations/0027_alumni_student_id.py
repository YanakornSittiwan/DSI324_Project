# Generated by Django 4.0.4 on 2022-05-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumTUapp', '0026_alter_course_campus_alter_course_course_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='Student_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
