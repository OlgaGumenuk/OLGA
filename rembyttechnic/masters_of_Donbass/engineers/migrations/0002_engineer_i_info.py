# Generated by Django 5.1.1 on 2024-09-25 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineer',
            name='i_info',
            field=models.TextField(blank=True),
        ),
    ]
