# Generated by Django 4.2.8 on 2023-12-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]