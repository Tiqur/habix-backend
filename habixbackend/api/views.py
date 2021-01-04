from django.views.decorators.csrf import csrf_exempt
from .models import HabixUser, DailyTask
from habix.serializers import HabixUserSerializer, DailyTaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class HabixUserList(ListCreateAPIView):
    queryset = HabixUser.objects.all()
    serializer_class = HabixUserSerializer


class HabixUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = HabixUser.objects.all()
    serializer_class = HabixUserSerializer


class DailyTaskList(ListCreateAPIView):
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer


class DailyTaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer
