from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Icons
from .serializers import *
# два метода: один все высерает, другой постранично по 10 штук
# категории иконок

class AllIconsAPIView(ListAPIView):
    queryset = Icons.objects.all()
    serializer_class = IconsSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:
            return Icons.objects.filter(category__name=category)
        return super().get_queryset()


class IconsPaginations(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page'


class PagesIconsAPIView(ListAPIView):
    queryset = Icons.objects.all().order_by('pk')
    serializer_class = IconsSerializer
    pagination_class = IconsPaginations
    

class CreateIconsAPIView(CreateAPIView):
    queryset = Icons.objects.all()
    serializer_class = IconsSerializer

