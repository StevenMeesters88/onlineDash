# Generated by Django 4.2.5 on 2023-10-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_document_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='upload_sequence',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
