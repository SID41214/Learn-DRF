import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

#for class based

# from django.utils.decorators import method_decorator
# from django.views import View

# @method_decorator(csrf_exempt,name='dispatch')
# class StudentAPI(View):
#     def get(self,request,*args, **kwargs):
#         json_data = request.body
#         stream =io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id',None)
#         if id is not None:
#             stu = Student.objects.get(id=id)   # pylint: disable=no-member
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
        
#         stu = Student.objects.all()  # pylint: disable=no-member
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
    
#     def post(self,request,*args, **kwargs):
#         json_data =request.body
#         stream = io.BytesIO(json_data)
#         python_data =JSONParser().parse(stream)
#         serializer = StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res ={'msg':'Data Created'}
#             json_data =JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type="application/json")
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type="application/json")
    
    
#     def put(self,request,*args, **kwargs):
#         json_data =request.body
#         stream =io.BytesIO(json_data)
#         python_data =JSONParser().parse(stream)
#         id =python_data.get('id')
#         stu = Student.objects.get(id=id)  # pylint: disable=no-member
#         #Complete update then , Required all data from frontend
#         #serializer = StudentSerializer(stu,data=python_data)
#         #Partial Update then , all data not required
#         serializer = StudentSerializer(stu,data=python_data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res ={'msg':'Data Updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data =JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_types='application/json')
    
#     def delete(self,request,*args, **kwargs):
#         json_data = request.body
#         stream=io.BytesIO(json_data)
#         python_data =JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu =Student.objects.get(id=id)   # pylint: disable=no-member
#         stu.delete()
#         res ={'msg':'Data Deleted'}
#         json_data=JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type='application/json')
        
        
        
        
        


    
    
         
        
    















@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream =io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)   # pylint: disable=no-member
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        stu = Student.objects.all()  # pylint: disable=no-member
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'POST':
        json_data =request.body
        stream = io.BytesIO(json_data)
        python_data =JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res ={'msg':'Data Created'}
            json_data =JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
    
    if request.method == 'PUT':
        json_data =request.body
        stream =io.BytesIO(json_data)
        python_data =JSONParser().parse(stream)
        id =python_data.get('id')
        stu = Student.objects.get(id=id)  # pylint: disable=no-member
        #Complete update then , Required all data from frontend
        #serializer = StudentSerializer(stu,data=python_data)
        #Partial Update then , all data not required
        serializer = StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res ={'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data =JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_types='application/json')
    
    
    if request.method == 'DELETE':
        json_data = request.body
        stream=io.BytesIO(json_data)
        python_data =JSONParser().parse(stream)
        id=python_data.get('id')
        stu =Student.objects.get(id=id)   # pylint: disable=no-member
        stu.delete()
        res ={'msg':'Data Deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
        
        
        