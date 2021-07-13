''' Определяет схемы URL для order '''

from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

app_name = 'order'

urlpatterns = [
	path('', views.order, name='order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
