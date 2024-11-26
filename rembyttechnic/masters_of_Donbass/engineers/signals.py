from django.db.models.signals import post_save, post_delete
from .models import Engineer
from django.contrib.auth.models import User

def create_engineer(sender, instance, created, **kwargs):
    if created:
        user = instance
        engineer = Engineer.objects.create(
            engineer=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


def delete_engineer(sender, instance, **kwargs):
    engineer = instance.engineer
    engineer.delete()


def update_engineer(sender, instance, created, **kwargs):
    engineer = instance  # экземпляр класса приходит польль в кот меняем
    user = engineer.engineer

    if created is False:
        user.first_name = engineer.name
        user.username = engineer.username
        user.email = engineer.email
        user.save()


post_save.connect(create_engineer, sender=User)
post_delete.connect(delete_engineer,  sender=Engineer)
post_save.connect(update_engineer, sender=Engineer)  # sender вызывает событие
