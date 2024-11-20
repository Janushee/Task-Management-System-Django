from rest_framework import serializers
from .models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    task = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'designation','task']

    def get_task(self, obj):
        from task.models import Task  # Import the Task model only
        from task.serializers import TaskStatusSerializer  # Import locally
        tasks = Task.objects.filter(assigned_to=obj)
        return TaskStatusSerializer(tasks, many=True).data




class EmployeeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']
