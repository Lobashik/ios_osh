from rest_framework.serializers import ModelSerializer

from .models import Icons


class IconsSerializer(ModelSerializer):
    class Meta:
        model = Icons
        fields = '__all__'
