# Generated by Django 3.1.2 on 2020-10-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0004_auto_20201001_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offering',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
