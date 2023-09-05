# Generated by Django 3.2 on 2023-08-29 18:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='users/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'png'))]),
        ),
    ]