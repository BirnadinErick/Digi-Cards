# Generated by Django 3.1.4 on 2020-12-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_flashcard_prerequisites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, related_name='requirements', to='main.SubUnit'),
        ),
    ]
