from rest_framework import serializers
from .models import Student




class StudentSerializer(serializers.ModelSerializer):
    # name =serializers.CharField(read_only=True) #cannot able to update ,it is in readonly mode
    class Meta:
        model = Student
        fields =['name','roll','city']
        # read_only_fields=['name','roll']
        # extra_kwargs = {'name':{'read_only':True}}




 
# class StudentSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=100)
    # roll = serializers.IntegerField()
    # city = serializers.CharField(max_length=100)
    
    # def create(self,validated_data):
    #     return Student.objects.create(**validated_data)  # pylint: disable=no-member
    
    # def update(self,instance,validated_data):
      
    #     instance.name = validated_data.get('name',instance.name)
      

    #     instance.roll = validated_data.get('roll',instance.roll)
    #     instance.city = validated_data.get('city',instance.city)
    #     instance.save()
    #     return instance
