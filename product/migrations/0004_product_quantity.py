# Generated by Django 3.2 on 2023-09-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.SmallIntegerField(default=0),
        ),
    ]
