# Generated by Django 3.1.2 on 2020-10-19 22:10

import builder.utils
import builder.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0021_remove_motherboardchipset_max_memory_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='image',
            field=models.ImageField(default='', upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cpu',
            name='image',
            field=models.ImageField(default='', upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cpucooler',
            name='image',
            field=models.ImageField(default='', upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gpu',
            name='image',
            field=models.ImageField(default='', upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hdd',
            name='image',
            field=models.ImageField(default='', upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memory',
            name='image',
            field=models.ImageField(default='', upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='image',
            field=models.ImageField(default='', upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='psu',
            name='image',
            field=models.ImageField(default='', upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ssd',
            name='image',
            field=models.ImageField(default='', upload_to=builder.utils.handle_upload, validators=[builder.validators.validate_image_extension]),
            preserve_default=False,
        ),
    ]
