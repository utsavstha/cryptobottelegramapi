from django.db import models
from django.utils import timezone
import random
import string
# Create your models here.

LANGUAGE_CHOICES = (
    ("en", "English"),
    ("es", "Spanish"),

)


class Bot(models.Model):
    bot_name = models.CharField(
        max_length=100, null=False)
    bot_language = models.CharField(
        max_length=20, choices=LANGUAGE_CHOICES,
        default='English', null=False)

    def __str__(self):
        return self.bot_name


class Lead(models.Model):
    bot = models.ForeignKey(
        Bot, null=True, related_name='Bot', on_delete=models.SET_NULL)
    full_name_seller = models.CharField(
        max_length=100, null=False)
    seller_whatsapp_number = models.CharField(max_length=50, null=False)
    seller_referral_link = models.CharField(max_length=50, null=False)
    telegram_bot_url = models.CharField(max_length=50, null=False)

    createdAt = models.DateTimeField(auto_now_add=True)

    # sport_icon = models.FileField(upload_to='files', blank=True)
    def save(self, *args, **kwargs):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(8))
        self.telegram_bot_url = result_str
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name_seller}, {self.seller_whatsapp_number}"


class Welcome(models.Model):
    bot = models.ForeignKey(
        Bot, null=True, on_delete=models.SET_NULL)
    content = models.TextField(null=False)
    continue_to_main_menu = models.CharField(
        max_length=50, null=False)

    class Meta:
        verbose_name_plural = 'Welcome'


class MainMenu(models.Model):
    bot = models.ForeignKey(
        Bot, null=True, on_delete=models.SET_NULL)
    content = models.TextField(null=False)
    presentation_pdf = models.CharField(
        max_length=50, null=False)
    presentation_videos = models.CharField(
        max_length=50, null=False)
    register = models.CharField(
        max_length=50, null=False)

    class Meta:
        verbose_name_plural = 'MainMenu'


class PresentationMenu(models.Model):
    bot = models.ForeignKey(
        Bot, null=True, on_delete=models.SET_NULL)
    content = models.TextField(null=False)
    register = models.CharField(
        max_length=50, null=False)
    more_info = models.CharField(
        max_length=50, null=False)
    main_menu = models.CharField(
        max_length=50, null=False)

    class Meta:
        verbose_name_plural = 'PresentationMenu'


class VideoMenu(models.Model):
    bot = models.ForeignKey(
        Bot, null=True, on_delete=models.SET_NULL)
    content = models.TextField(null=False)

    register = models.CharField(
        max_length=50, null=False)
    main_menu = models.CharField(
        max_length=50, null=False)

    class Meta:
        verbose_name_plural = 'VideoMenu'


class VideoMenuOption(models.Model):
    videoMenu = models.ForeignKey(
        VideoMenu, related_name='VideoMenu', on_delete=models.CASCADE)
    content = models.CharField(max_length=50, null=False)

    url = models.CharField(
        max_length=200, null=False)

    class Meta:
        verbose_name_plural = 'VideoMenuOption'


class BotUser(models.Model):
    first_name = models.CharField(
        max_length=50, null=True)
    last_name = models.CharField(
        max_length=50, null=True)

    language_code = models.CharField(
        max_length=50, null=True)

    telegram_id = models.CharField(
        max_length=50, null=True)

    lead = models.ForeignKey(
        Lead, related_name='BotUser', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'BotUser'


class RegisterMenu(models.Model):
    bot = models.ForeignKey(
        Bot, null=True, on_delete=models.SET_NULL)
    content = models.TextField(null=True)

    main_menu = models.CharField(
        max_length=50, null=True)

    class Meta:
        verbose_name_plural = 'RegisterMenu'

    def __str__(self):
        return f"{self.bot}, {self.content}, {self.main_menu}"
