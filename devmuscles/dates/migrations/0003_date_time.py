# Generated by Django 3.2.7 on 2021-09-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dates', '0002_alter_date_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='time',
            field=models.IntegerField(default=1000),
        ),
    ]