# Generated by Django 2.1 on 2020-11-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_price', '0009_pack_contrast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='contrast',
            field=models.TextField(default='', max_length=400),
        ),
    ]