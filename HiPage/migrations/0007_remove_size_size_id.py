# Generated by Django 2.1.7 on 2019-06-07 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HiPage', '0006_good_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='Size_id',
        ),
    ]