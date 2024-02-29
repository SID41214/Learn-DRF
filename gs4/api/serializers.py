from rest_framework import serializers
from .models import Student

# Validators

def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name must start with r ")
    






class StudentSerializer(serializers.Serializer):
    #id = serializers.IntegerField()
    name = serializers.CharField(max_length=100,validators =[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self,validated_data):
        return Student.objects.create(**validated_data)  # pylint: disable=no-member
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    #Feild level validation
    def validate_roll(self,value):   #for validation of roll feild of student serializer 
        if value >= 200:
            raise serializers.ValidationError(" Seat Full")
        return value
      
    
    # Object level validation
    def validate(self,data):
        nm =data.get('name')
        ct =data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError("City must to be rachi")
        return data
      

