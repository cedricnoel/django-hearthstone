"""hearthstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from cards import views as cardViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', cardViews.IndexView.as_view(), name='hearthstone-index'),
	path('cards/', include('cards.urls')),
    path('decks/', include('decks.urls')),
    path('forum/', include('forum.urls')),
    path('admin/', admin.site.urls),
    path('packet/', include('packet.urls')),
    path('', include('user.urls', namespace="User")),
    path('challenge/', include('challenge.urls')),
    path('social/', include('social.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
