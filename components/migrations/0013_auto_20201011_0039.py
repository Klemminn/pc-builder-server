# Generated by Django 3.1.2 on 2020-10-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0012_auto_20201010_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdd',
            name='format',
            field=models.CharField(max_length=20),
        ),
    ]
