# Generated by Django 2.1 on 2020-11-19 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_price', '0006_pack_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='formula',
            new_name='cost',
        ),
        migrations.AddField(
            model_name='pack',
            name='_10000_20000',
            field=models.CharField(default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='pack',
            name='_20000_50000',
            field=models.CharField(default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='pack',
            name='_50000',
            field=models.CharField(default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='pack',
            name='_5000_10000',
            field=models.CharField(default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='pack',
            name='edition_fee',
            field=models.CharField(default='', max_length=500),
        ),
    ]
