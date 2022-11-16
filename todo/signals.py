from django.contrib.auth.models import  User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from rest_framework.authtoken.views import Token



@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    """
    Creates a new user with token dynamically cretaed.
    """
    if created:
        Token.objects.create(user=instance)


@receiver(pre_delete, sender=User)
def delete_user_token(sender, instance, **kwargs):
    """
    Deletes a token associated with a user when that user is deleted.
    """
    token = Token.objects.get(user=instance)
    token.delete()
