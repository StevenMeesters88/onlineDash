# Generated by Django 4.2.5 on 2023-10-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='session_key',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
