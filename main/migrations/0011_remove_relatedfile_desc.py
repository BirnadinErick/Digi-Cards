# Generated by Django 3.1.4 on 2020-12-22 05:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0010_auto_20201222_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatedfile',
            name='desc',
        ),
    ]
