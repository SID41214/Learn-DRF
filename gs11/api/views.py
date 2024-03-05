from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,ListCreateAPIView


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    