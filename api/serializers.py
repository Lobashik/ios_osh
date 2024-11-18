from rest_framework.serializers import ModelSerializer

from .models import Icons, Category


class IconsSerializer(ModelSerializer):
    class Meta:
        model = Icons
        fields = '__all__'


class CreateIconsSerializer(ModelSerializer):
    class Meta:
        model = Icons
        exclude = ('id',)
        

class CreateCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)
        

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'