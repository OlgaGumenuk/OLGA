from django.db import models
from django.contrib.auth.models import User


class Engineer(models.Model):
    engineer = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, verbose_name="Мастер")
    name = models.CharField(max_length=200, blank=True, verbose_name="Имя")
    email = models.EmailField(max_length=200, blank=True, verbose_name="Email")
    username = models.CharField(max_length=200, blank=True, verbose_name="Username")
    i_info = models.TextField(max_length=100, blank=True, verbose_name="Кратко")
    all_info = models.TextField(blank=True, verbose_name="Информация")
    engineer_image = models.ImageField(upload_to="repairs/", default="repairs/engineer.jpeg", verbose_name="Фото")
    education = models.CharField(max_length=200, blank=True, verbose_name="Образование")
    price = models.FileField(upload_to="repairs/", default="repairs/price_repair_cleaner.jpeg", verbose_name="Цены")
    social_website = models.CharField(max_length=200, blank=True, verbose_name="Сайт")
    social_vkontakte = models.CharField(max_length=200, blank=True, verbose_name="Вконтакте")
    social_whatsapp = models.CharField(max_length=200, blank=True, verbose_name="WhatsApp")
    social_telegram = models.CharField(max_length=200, blank=True, verbose_name="Телеграм")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.username




