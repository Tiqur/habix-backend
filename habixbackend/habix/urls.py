from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', views.HabixUserList.as_view()),
    path('api/users/<int:pk>', views.HabixUserDetail.as_view()),
    path('api/tasks/', views.DailyTaskList.as_view()),
    path('api/tasks/<int:pk>', views.DailyTaskDetail.as_view()),
]
