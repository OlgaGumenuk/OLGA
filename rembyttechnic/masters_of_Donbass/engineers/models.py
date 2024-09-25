from django.db import models
from django.contrib.auth.models import User


class Engineer(models.Model):
    engineer = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    username = models.CharField(max_length=200, blank=True)
    all_info = models.TextField(blank=True)
    engineer_image = models.ImageField(upload_to="repairs/", default="repairs/engineer.jpeg")
    education = models.TextField(max_length=200, blank=True)
    price = models.FileField(upload_to="repairs/", default="repairs/price_repair_cleaner.jpeg")
    social_yandex = models.CharField(max_length=200, blank=True)
    social_vkontakte = models.CharField(max_length=200, blank=True)
    social_whatsapp = models.CharField(max_length=200, blank=True)
    social_telegramm = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username







