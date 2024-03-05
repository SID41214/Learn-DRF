from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,ListCreateAPIView,DestroyAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer


class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    

class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer













# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer


# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer
    

# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentLC(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentRU(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentRD(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentRUD(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer

