# Generated by Django 3.1.2 on 2021-05-21 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerings', '0011_scrape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offering',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
