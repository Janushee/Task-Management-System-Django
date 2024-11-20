from django.urls import path
from .views import CreateTask,GetTask,ChangeStatus,GetSubtask

urlpatterns = [
    path('', CreateTask.as_view()),
    path('get-task', GetTask.as_view()),
    path('<int:id>/status/', ChangeStatus.as_view()),
    path('<int:id>/subtasks/',GetSubtask.as_view())

]