# Generated by Django 3.1.5 on 2021-01-19 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='examcompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
