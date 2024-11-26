from django.db import models
from engineers.models import Engineer


class Repair(models.Model):
    owner = models.ForeignKey(Engineer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Мастер")
    type_of_repair = models.CharField(max_length=200, verbose_name="Вид ремонта")
    description = models.TextField(blank=True, verbose_name="Описание")
    my_image = models.ImageField(default="resize_imag.jpg", upload_to='repairs/%Y/%m/%d', verbose_name="Фото")
    price_link = models.FileField(upload_to="repairs/", default="repairs/price_repair_cleaner.jpeg", verbose_name="Цены")
    vote_total = models.IntegerField(default=0, blank=True, verbose_name="Отзывов")
    vote_ratio = models.IntegerField(default=0, blank=True, verbose_name="Положительных отзывов")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата")


    def __str__(self):
        return self.type_of_repair


    class Meta:
        ordering = ["-created"]





