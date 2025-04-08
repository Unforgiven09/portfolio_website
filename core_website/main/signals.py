from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import ProductImage


@receiver(post_delete, sender=ProductImage)
def delete_files(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
    if instance.thumbnail:
        instance.thumbnail.delete(save=False)