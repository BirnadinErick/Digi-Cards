# Generated by Django 3.1.4 on 2020-12-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_auto_20201217_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='prerequisites',
            field=models.ManyToManyField(related_name='requirements', to='main.SubUnit'),
        ),
    ]
