from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
#  Model Object -Single Student Data
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)  # pylint: disable=no-member
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')