# Generated by Django 3.1.3 on 2021-04-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]
