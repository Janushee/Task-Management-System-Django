from django.urls import path
from .views import CreateEmployee,GetEmployee,GetEmployeeTasks

urlpatterns = [
    path('', CreateEmployee.as_view()),
    path('get-employee/', GetEmployee.as_view()),
    path('<int:id>/tasks/', GetEmployeeTasks.as_view()),

]