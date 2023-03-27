from django.contrib import admin
from .models import Lead, Bot, Welcome, MainMenu, PresentationMenu, VideoMenu, VideoMenuOption, BotUser, RegisterMenu
# Register your models here.


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('full_name_seller', 'seller_whatsapp_number',
                    'seller_referral_link', 'telegram_bot', 'bot')
    exclude = ('telegram_bot_url',)

    def telegram_bot(self, obj):
        return f"https://t.me/{obj.bot.bot_name}?start={obj.telegram_bot_url}"


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('bot_name', 'bot_language')
    exclude = ('telegram_bot_url',)


@admin.register(Welcome)
class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('content', 'bot')


@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('content', 'bot')


@admin.register(PresentationMenu)
class PresentationMenuAdmin(admin.ModelAdmin):
    list_display = ('content', 'bot')


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'lead')


@admin.register(RegisterMenu)
class RegisterMenuAdmin(admin.ModelAdmin):
    list_display = ('bot', 'content')


class VideoMenuOptionInline(admin.TabularInline):
    model = VideoMenuOption


@admin.register(VideoMenu)
class VideoMenuMenuAdmin(admin.ModelAdmin):
    list_display = ('content', 'bot')
    inlines = [
        VideoMenuOptionInline,
    ]
