from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from .models import NewsLetter, NewsLetterUsers, PrayerRequest, VideoMessage
 
 
@receiver(post_save, sender=NewsLetter)
def send_newsletter_emails(sender, instance, created, **kwargs):
    print('this ran succcessfully thank god')
    news_letter = instance
    if created:
        news_letter_emails = [user.email for user in NewsLetterUsers.objects.all()]
        send_mail(
            news_letter.subject,
            news_letter.body,
            settings.EMAIL_HOST_USER,
            news_letter_emails,
            fail_silently=False,
        )

@receiver(post_save, sender=PrayerRequest)
def send_prayer_request(sender, instance, created, **kwargs):
    if created:
        # sending email with user prayer request
        send_mail(
            f"Prayer request from { instance.firstname } {instance.lastname}",
            instance.request,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

@receiver(pre_save, sender=VideoMessage)
def delete_older_videos(sender, instance, **kwargs):
    VideoMessage.objects.all().delete()
