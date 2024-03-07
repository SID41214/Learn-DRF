from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser




class StudentModelViewSet(viewsets.ModelViewSet):   #only need this for CRUD operations
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes =[AllowAny]
    # permission_classes =[IsAdminUser]