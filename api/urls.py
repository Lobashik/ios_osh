from django.urls import path

from .views import *


urlpatterns = [
    path('all_icons/', AllIconsAPIView.as_view()),
    path('icons/', PagesIconsAPIView.as_view()),
]