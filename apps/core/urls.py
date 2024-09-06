from django.urls import path, re_path, include
from django.utils.translation import gettext_lazy as _

from .views import home

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
]
