from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskStatusSerializer,TaskSubtaskSerilizer,TaskSerializer

# Create your views here.
class CreateTask(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class GetTask(APIView):
    def get(self, request):
        user = Task.objects.all()
        serializer = TaskSerializer(user,many=True)
        return Response(serializer.data)

class ChangeStatus(APIView):
    def patch(self,request,id):
        result = Task.objects.get(id=id)
        serializer = TaskStatusSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"status": "error", "data": serializer.errors})

class GetSubtask(APIView):
    def get(self, request,id):
        task = Task.objects.get(id=id)
        serializer = TaskSubtaskSerilizer(task)
        return Response(serializer.data)