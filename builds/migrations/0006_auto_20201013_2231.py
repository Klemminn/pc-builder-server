# Generated by Django 3.1.2 on 2020-10-13 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0005_auto_20201012_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='offerings',
            field=models.JSONField(unique=True),
        ),
    ]