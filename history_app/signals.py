from django.db.models.signals import post_save
from django.dispatch import receiver
from tweet_app.models import Tweet
from .models import History


@receiver(post_save, sender=Tweet)
def create_history_on_tweet_save(sender, instance, created, **kwargs):
    if created:
        summary_text = f"User {instance.user.username} Created tweet with a content of '{instance.content}' at {instance.created_at}"

        History.objects.create(
            user=instance.user,
            method="POST",
            tweet=instance,
            date=instance.created_at,
            summary=summary_text
        )


