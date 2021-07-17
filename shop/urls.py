''' Определяет схемы URL для shop '''

from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'shop'

urlpatterns = [
	path('catalog/', views.shop, name='catalog'),
]
