# Generated by Django 2.1.7 on 2019-05-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Available', models.CharField(max_length=50)),
                ('Photo', models.ImageField(upload_to='clothes_photos')),
            ],
        ),
    ]
