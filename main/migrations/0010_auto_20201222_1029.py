# Generated by Django 3.1.4 on 2020-12-22 04:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0009_auto_20201222_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='last_updated',
            field=models.DateField(blank=True),
        ),
    ]
