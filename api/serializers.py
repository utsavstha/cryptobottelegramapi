from core.models import Lead, Bot, Welcome, MainMenu, PresentationMenu, VideoMenu, VideoMenuOption, BotUser, RegisterMenu
from rest_framework import serializers


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = "__all__"


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = '__all__'


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        lookup_field = 'telegram_bot_url'
        extra_kwargs = {
            'url': {'lookup_field': 'telegram_bot_url'}
        }


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome
        fields = '__all__'


class MainMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMenu
        fields = '__all__'


class PresentationMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentationMenu
        fields = '__all__'


class VideoMenuOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMenuOption
        fields = '__all__'


class VideoMenuSerializer(serializers.ModelSerializer):
    VideoMenu = VideoMenuOptionSerializer(many=True, read_only=True)

    class Meta:
        model = VideoMenu
        fields = ['content', 'register', 'main_menu', 'bot', 'VideoMenu']


class RegisterMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterMenu
        fields = '__all__'
