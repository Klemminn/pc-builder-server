# Generated by Django 3.1.2 on 2020-10-01 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_auto_20201001_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpu',
            name='boost_clock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gpu',
            name='core_clock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gpu',
            name='memory',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gpu',
            name='tdp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storage',
            name='capacity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storage',
            name='read_speed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storage',
            name='write_speed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]