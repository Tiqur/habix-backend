from rest_framework import serializers
from api.models import HabixUser, DailyTask

class HabixUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabixUser
        fields = ['uuid', 'timezone']

class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTask
        fields = ['uuid', 'timezone', 'task_name', 'streak_graph', 'created_at', 'best_streak']
