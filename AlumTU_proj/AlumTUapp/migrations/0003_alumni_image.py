# Generated by Django 4.0.3 on 2022-04-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumTUapp', '0002_alter_alumni_user_id_delete_sys_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pic'),
        ),
    ]
