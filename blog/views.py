from django.db.models import query_utils
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MaqolaViewSet(ModelViewSet):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def perform_create(self, serializer):
        serializer.save(self.request.user)
    
    def get_queryset(self):
        return Maqola.objects.all()
    




    @action(detail=True,methods=['GET'])
    def rasm(self, request, *args, **kwargs):
        maqola = self.get_object()
        serializer = RasmSerializer(maqola.rasm_set.all(), many = True)
        return Response(serializer.data)

class RasmViewSet(ModelViewSet):
    queryset = Rasm.objects.all()
    serializer_class = RasmSerializer
    @action(detail=True, methods=['GET'])
    def maqola(self, request, *args, **kwargs):
        rasm = self.get_object()
        maqola = Maqola.objects.get(id=rasm.maqolaid.id)
        serializer = MaqolaSerializer(maqola)
        return Response(serializer.data)