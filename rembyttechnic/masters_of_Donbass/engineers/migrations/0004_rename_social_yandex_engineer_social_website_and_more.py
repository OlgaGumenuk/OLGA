# Generated by Django 5.1.1 on 2024-09-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineers', '0003_rename_social_telegramm_engineer_social_telegram_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='engineer',
            old_name='social_yandex',
            new_name='social_website',
        ),
        migrations.AlterField(
            model_name='engineer',
            name='education',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]