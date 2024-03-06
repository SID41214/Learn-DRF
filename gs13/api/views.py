from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets




class StudentModelViewSet(viewsets.ModelViewSet):   #only need this for CRUD operations
    queryset = Student.objects.all()
    serializer_class = StudentSerializer