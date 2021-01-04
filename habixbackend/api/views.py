from django.views.decorators.csrf import csrf_exempt
from .models import HabixUser, DailyTask
from habix.serializers import HabixUserSerializer, DailyTaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

class HabixUserList(ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = HabixUser.objects.all()
    serializer_class = HabixUserSerializer


class HabixUserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = HabixUser.objects.all()
    serializer_class = HabixUserSerializer


class DailyTaskList(ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer


class DailyTaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer
