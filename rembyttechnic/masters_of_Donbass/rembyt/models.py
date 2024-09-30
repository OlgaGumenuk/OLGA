from django.db import models
from engineers.models import Engineer


class Repair(models.Model):
    owner = models.ForeignKey(Engineer, on_delete=models.SET_NULL, blank=True, null=True)
    type_of_repair = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    my_image = models.ImageField(default="resize_imag.jpg", upload_to='repairs/%Y/%m/%d')
    price_link = models.FileField(upload_to="repairs/", default="repairs/price_repair_cleaner.jpeg")
    vote_total = models.IntegerField(default=0, blank=True)
    vote_ratio = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.type_of_repair
