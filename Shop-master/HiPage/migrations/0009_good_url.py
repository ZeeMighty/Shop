# Generated by Django 2.1.7 on 2019-06-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiPage', '0008_good_get'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='URL',
            field=models.URLField(default=' '),
        ),
    ]