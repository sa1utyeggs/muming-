# Generated by Django 2.1 on 2020-11-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_price', '0012_remove_pack_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack',
            name='remarks',
            field=models.TextField(default='备注：无', max_length=300),
        ),
    ]