from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, status
from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from core.models import Bot, Lead, Welcome, MainMenu, PresentationMenu, VideoMenu, BotUser, RegisterMenu
from api.serializers import BotSerializer, LeadSerializer, WelcomeSerializer, MainMenuSerializer, PresentationMenuSerializer, VideoMenuSerializer, BotUserSerializer, RegisterMenuSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

# Create your views here.


# class BotsViewSet(viewsets.ViewSet):
#     queryset = Bot.objects.all()

#     def list(self, request):
#         botModel = None
#         url = None
#         if 'telegram_bot_url' in request.data:
#             url = request.data['telegram_bot_url']
#         if url:
#             telegram_bot = f"https://t.me/ibookaudiobot?start={url}"

#             botModel = Bot.objects.filter(telegram_bot_url=telegram_bot)
#         else:
#             botModel = Bot.objects.all()
#         botSerializer = BotSerializer(botModel, many=True)
#         return Response(
#             {
#                 'bots': botSerializer.data,
#             }
#         )


class LeadsViewSet(viewsets.ViewSet):
    queryset = Lead.objects.all()

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, telegram_bot_url=pk)
        serializer = LeadSerializer(item)
        return Response(serializer.data)


class WelcomeViewSet(viewsets.ViewSet):
    queryset = Welcome.objects.all()

    def retrieve(self, request, pk=None):
        print(pk)
        bot = Bot.objects.filter(bot_language=pk).first()
        print(bot)
        item = get_object_or_404(self.queryset, bot=bot)
        serializer = WelcomeSerializer(item)
        return Response(serializer.data)


class MainMenuViewSet(viewsets.ViewSet):
    queryset = MainMenu.objects.all()

    def retrieve(self, request, pk=None):
        print(pk)
        bot = Bot.objects.filter(bot_language=pk).first()
        item = get_object_or_404(self.queryset, bot=bot)
        serializer = MainMenuSerializer(item)
        return Response(serializer.data)


class PresentationMenuViewSet(viewsets.ViewSet):
    queryset = PresentationMenu.objects.all()

    def retrieve(self, request, pk=None):
        print(pk)
        bot = Bot.objects.filter(bot_language=pk).first()
        item = get_object_or_404(self.queryset, bot=bot)
        serializer = PresentationMenuSerializer(item)
        return Response(serializer.data)


class VideoMenuViewSet(viewsets.ViewSet):
    queryset = VideoMenu.objects.all()

    def retrieve(self, request, pk=None):
        print(pk)
        bot = Bot.objects.filter(bot_language=pk).first()
        item = get_object_or_404(self.queryset, bot=bot)
        serializer = VideoMenuSerializer(item)
        return Response(serializer.data)


# class RegisterMenuView(generics.RetrieveDestroyAPIView):
#     # serializer_class = RegisterMenuSerializer
#     queryset = RegisterMenu.objects.all()

#     def get_object(self):
#         bot_language = self.kwargs["bot_language"]
#         telegram_id = self.kwargs["telegram_id"]
#         bot = Bot.objects.filter(bot_language=bot_language).first()
#         data = RegisterMenu.objects.filter(bot=bot)
#         registerSerializer = RegisterMenuSerializer(data)
#         user = BotUser.objects.filter(telegram_id=telegram_id)
#         serializer = BotUserSerializer(user)
#         return Response(serializer.data)
#         # queryset = RegisterMenu.objects.filter(customer_id=self.kwargs["customer_pk"]).get(order_number=self.kwargs["pk"])
#         # return queryset
class RegisterMenuViewSet(viewsets.ViewSet):
    queryset = RegisterMenu.objects.all()
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        data = JSONParser().parse(request)
        bot_language = data["bot_language"]
        telegram_id = data["telegram_id"]
        bot = Bot.objects.filter(bot_language=bot_language).first()
        data = get_object_or_404(self.queryset, bot=bot)
        registerSerializer = RegisterMenuSerializer(data)
        user = BotUser.objects.filter(telegram_id=telegram_id).first()

        serializer = LeadSerializer(user.lead)
        return Response({"register_data": registerSerializer.data, "lead": serializer.data})


class BotUserViewSet(viewsets.ViewSet):
    queryset = BotUser.objects.all()
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        data = JSONParser().parse(request)
        user = BotUser.objects.filter(telegram_id=data['telegram_id']).count()
        if user > 0:
            serializer = BotUserSerializer(user)
            return JsonResponse({}, status=200)
        else:
            lead = Lead.objects.filter(
                telegram_bot_url=data['registration_link']).first()
            print(lead)
            user = BotUser.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                language_code=data['language_code'],
                telegram_id=data['telegram_id'],
                lead=lead
            )
            serializer = BotUserSerializer(user)

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        telegram_bot_url = f"https://t.me/ibookaudiobot?start={pk}"
        lead = Lead.objects.filter(telegram_bot_url=telegram_bot_url).first()
        item = get_object_or_404(self.queryset, lead=lead)
        serializer = BotUserSerializer(item)
        return Response(serializer.data)
