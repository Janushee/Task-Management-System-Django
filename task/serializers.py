from requests import request
from rest_framework import serializers
from .models import Task

from employee.models import Employee

from employee.serializers import EmployeeTaskSerializer

class TaskSerializer(serializers.ModelSerializer):

    assigned_to_details = EmployeeTaskSerializer(
        source='assigned_to', read_only=True
    )  # Outputs nested employee details

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'due_date', 'assigned_to', 'assigned_to_details'
        ]

class TaskStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'status']



class TaskSubtaskSerilizer(serializers.ModelSerializer):
    task=TaskSerializer()
    subtasks=serializers.RelatedField(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ['task','subtasks']