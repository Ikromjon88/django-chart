# Generated by Django 4.0 on 2022-04-05 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mazmuni',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]
