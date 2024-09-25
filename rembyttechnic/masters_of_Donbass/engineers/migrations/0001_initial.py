# Generated by Django 5.1.1 on 2024-09-25 12:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('username', models.CharField(blank=True, max_length=200)),
                ('all_info', models.TextField(blank=True)),
                ('engineer_image', models.ImageField(default='repairs/engineer.jpeg', upload_to='repairs/')),
                ('education', models.TextField(blank=True, max_length=200)),
                ('price', models.FileField(default='repairs/price_repair_cleaner.jpeg', upload_to='repairs/')),
                ('social_yandex', models.CharField(blank=True, max_length=200)),
                ('social_vkontakte', models.CharField(blank=True, max_length=200)),
                ('social_whatsapp', models.CharField(blank=True, max_length=200)),
                ('social_telegramm', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('engineer', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
