from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
class CreateEmployee(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class GetEmployee(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)

class GetEmployeeTasks(APIView):
    def get(self,request,id):
        employees = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data)


