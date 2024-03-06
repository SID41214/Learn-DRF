from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets



class  StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("********* List ************")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        stu =Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    
    def retrieve(self,request, pk=None):
        print("********* Retrieve ************")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        try:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # id = pk
        # if id is not None:
        #     stu =Student.objects.all()
        #     serializer=StudentSerializer(stu,many=True)
        #     return Response(serializer.data)
        
    
    
    def create(self,request):
        print("********* Create ************")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        serializer =StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def update(self,request):
        print("********* Update ************")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
  
        
    
    def partial_update(self,request):
        print("********* Partial Update ************")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if  serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'})
        return Response(serializer.errors)
        
    
    def destroy(self,request):
        print("********* Destroy ************")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        id=pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
  
        
 





















# ------------------------First I Followed  this --------------------------

# class StudentViewSet(viewsets.ViewSet):
#     def list(self,request):
#         stu = Student.objects.all() #pylint : disable=no-member
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)
    
#     # def retrieve(self,request,pk=None):  this is not showing (assertion error)
#     #     id=pk
#     #     if id is None:
#     #         stu = Student.objects.get(id=id)
#     #         serializer = StudentSerializer(stu)
#     #         return Response(serializer.data)
#     def retrieve(self, request, pk=None):
#         try:
#             stu = Student.objects.get(pk=pk)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
            
#     def create(self,request):
#         serializer =StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created successfully'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self,request,pk):
#         id=pk
#         stu = Student.objects.get(pk=id)
#         serializer =StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def partial_update(self,request,pk):
#         id=pk
#         stu = Student.objects.get(pk=id)
#         serializer =StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors)
    
#     def destroy(self,request,pk):
#         id=pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})
        
        
        
        
            