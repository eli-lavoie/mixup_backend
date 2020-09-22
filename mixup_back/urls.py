"""mixup_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from mixupAPI.models import *
from mixupAPI.views import s3_link
from mixupAPI.views import register_user, login_user
from mixupAPI.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'genres', Genres, 'genre')
router.register(r'tracks', Tracks, 'track')
router.register(r'artists', Artists, 'artist')
router.register(r'files', Track_Files, 'file')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user),
    path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('create_signed_link', s3_link.as_view(), name='s3_link'),
]
