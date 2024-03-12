from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

from api.throttling import JackRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):   
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # throttle_classes = [AnonRateThrottle,JackRateThrottle]    #for user name jack which changed in the settings to 3/minutes