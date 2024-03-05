#GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin



# List And Create - pk not required
class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()         # pylint: disable=no-member
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
    

# Retrieve update and Destroy - pk Required

class RUDStudentAPI(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()         # pylint: disable=no-member
    serializer_class = StudentSerializer
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    
    
     








#-----------------------------------------------------------------------------------------------------------------------------
#------------------BY GenericAPIView and ModelMixin for which of having separate url in urls.py ------------------------------
#-----------------------------------------------------------------------------------------------------------------------------

# class StudentList(GenericAPIView,ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)


# class StudentCreate(GenericAPIView,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class StudentRetrive(GenericAPIView,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)


# class StudentUpdate(GenericAPIView,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)


# class StudentDestroy(GenericAPIView,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)
    
    
    
#-------------------------------------------------------------

# ---------------------Previous one --------------------------



# from django.shortcuts import render
# # from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status
# from rest_framework.views import APIView
# # Create your views here.

# class StudentAPI(APIView):
#     def get(self,request,pk=None,format=None):
#         id =pk
#         if id is not None:
#             stu =Student.objects.get(id=id)   # pylint: disable=no-member
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
            
#         stu = Student.objects.all()     # pylint: disable=no-member
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
    
#     def post(self,request,format=None):
#         serializer =StudentSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self,request,pk,format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)    # pylint: disable=no-member
#         serializer = StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk,format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)     # pylint: disable=no-member
#         stu.delete()
#         return Response({'msg':'Data deleted'})
    
#     def patch(self,request,pk,format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)    # pylint: disable=no-member
#         serializer = StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':' Partial Data updated'})
#         return Response(serializer.errors)
        
    
    







