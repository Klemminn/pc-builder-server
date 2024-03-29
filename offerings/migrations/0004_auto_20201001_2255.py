# Generated by Django 3.1.2 on 2020-10-01 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('offerings', '0003_offering_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='disabled',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='offering',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='offering',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
