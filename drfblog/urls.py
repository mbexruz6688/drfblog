from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from blog.views import *
from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter
from blog.views import MaqolaViewSet, RasmViewSet


router = DefaultRouter()
router.register('maqola', MaqolaViewSet, basename='maqola')
router.register('rasm', RasmViewSet, basename='rasm')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_token/', views.obtain_auth_token),
    path('', include(router.urls)),
]