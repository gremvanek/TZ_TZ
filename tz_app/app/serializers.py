from rest_framework.serializers import ModelSerializer

from tz_app.app.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'