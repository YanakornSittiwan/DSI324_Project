# Generated by Django 4.0.3 on 2022-04-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlumTUapp', '0016_alter_company_industry_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Sector',
            field=models.CharField(choices=[('บริษัทเอกชน', 'บริษัทเอกชน'), ('รัฐวิสาหกิจ', 'รัฐวิสาหกิจ'), ('หน่วยงานของรัฐ', 'หน่วยงานของรัฐ')], max_length=50),
        ),
    ]
