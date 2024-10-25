from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

import os
from tz_app.app.models import Item
from tz_app.app.serializers import ItemSerializer
from tz_app.tz_app import settings


def log_to_file(action, item_data):
    log_file_path = os.path.join(settings.BASE_DIR, 'changes_log.txt')
    with open(log_file_path, 'a') as f:
        f.write(f'{action}:{item_data}\n')

        
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
