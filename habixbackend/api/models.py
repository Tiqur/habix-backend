from django.db import models

class HabixUser(models.Model):
    uuid = models.BigIntegerField(primary_key=True)
    timezone = models.IntegerField(verbose_name='UTC offset') # UTC offset


class DailyTask(HabixUser):
    task_name = models.CharField(max_length=200)
    streak_graph = models.CharField(max_length=50000) # can hold ~130 years of data
    created_at = models.DateField(auto_now_add=True)
    best_streak = models.PositiveIntegerField(default=0)
