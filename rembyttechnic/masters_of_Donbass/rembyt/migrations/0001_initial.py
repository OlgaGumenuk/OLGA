# Generated by Django 5.1.1 on 2024-09-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_repair', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('my_image', models.ImageField(default='resize_imag.jpg', upload_to='repairs/%Y/%m/%d')),
                ('price_link', models.CharField(blank=True, max_length=200)),
                ('vote_total', models.IntegerField(blank=True, default=0)),
                ('vote_ratio', models.IntegerField(blank=True, default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
