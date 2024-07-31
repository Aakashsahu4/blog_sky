from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models as blog_model
from account import models as account_models


@receiver(post_save, sender=blog_model.Blog)
def create_notification(sender, instance, created, **kwargs):

    if created:
        users = account_models.User.objects.exclude(id=instance.user_profile.id)
        for user in users:
            blog_model.Notification.objects.get_or_create(from_user=instance.user_profile,to_user=user,blog=instance,notification_text=f'',)
    return True