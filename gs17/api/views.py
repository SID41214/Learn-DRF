from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class StudentModelViewSet(viewsets.ModelViewSet):   
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]