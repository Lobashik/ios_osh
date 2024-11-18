from django.urls import path

from .views import *


urlpatterns = [
    path('all_icons/', AllIconsAPIView.as_view()),
    path('icons/', PagesIconsAPIView.as_view()),
    path('create_icons/', CreateIconsAPIView.as_view()),
    path('create_category/', CreateCategoryAPIView.as_view()),
]