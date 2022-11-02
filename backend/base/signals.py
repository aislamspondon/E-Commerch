from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def updateUser(sender, instance, **kwargs):
    # print(f"{instance} => Instance \n {sender} => Sender \n {kwargs} => Kwarg")
    user = instance
    if user.email != '':
        user.username = user.email.split('@')[0]
