# Generated by Django 3.1.2 on 2020-10-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0008_auto_20201003_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='boost_clock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
