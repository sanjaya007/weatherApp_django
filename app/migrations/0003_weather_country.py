# Generated by Django 3.2.6 on 2021-09-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_weather_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]