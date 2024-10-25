from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


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

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            log_to_file('Created', response.data)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            log_to_file('Updated', response.data)
        return response
    
    def destroy(self, request, *args, **kwargs):
        i = self.get_object()
        self.perform_destroy(i)
        log_to_file('Deleted', {'id': i.id, 'name': i.name})
        return Response(status=status.HTTP_204_NO_CONTENT)

