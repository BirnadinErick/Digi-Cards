# Generated by Django 3.1.4 on 2020-12-21 01:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0007_auto_20201221_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatedfile',
            name='file',
            field=models.FileField(upload_to='related_files/'),
        ),
    ]
