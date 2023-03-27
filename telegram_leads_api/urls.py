"""telegram_leads_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from api import views as apiViews

router = DefaultRouter()
# router.register(f"bots", apiViews.BotsViewSet)
router.register(f"leads", apiViews.LeadsViewSet)
router.register(f"welcome", apiViews.WelcomeViewSet)
router.register(f"mainmenu", apiViews.MainMenuViewSet)
router.register(f"presentationMenu", apiViews.PresentationMenuViewSet)
router.register(f"videoMenu", apiViews.VideoMenuViewSet)
router.register(f"botuser", apiViews.BotUserViewSet)
router.register(f"register", apiViews.RegisterMenuViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/', include(router.urls)),
    # path('api/register/<str:bot_language>/<str:telegram_id>/',
    #      apiViews.RegisterMenuView.as_view()),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'
# default: "Django Administration"
admin.site.site_header = 'Bots Manager'
# default: "Site administration"
admin.site.index_title = 'Bots Manager'
admin.site.site_title = 'Bots Manager'  # default: "Django site admin"
