# Generated by Django 5.1.1 on 2024-09-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineers', '0002_engineer_i_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='engineer',
            old_name='social_telegramm',
            new_name='social_telegram',
        ),
        migrations.AlterField(
            model_name='engineer',
            name='education',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='engineer',
            name='i_info',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
