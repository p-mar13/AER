# Generated by Django 4.1.3 on 2023-05-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aer", "0002_textfile_data_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="textfile", name="file", field=models.FileField(upload_to=""),
        ),
    ]
