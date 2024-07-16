from .models import Employee
from rest_framework import serializers

# class Employeeserializer(serializers.Serializer):
#     name= serializers.CharField(max_length=40)
#     email=   serializers.EmailField( ) 
#     password= serializers.CharField(max_length=40)
#     phone= serializers.IntegerField( )

#     def create(self,validated_data):
#        return Employee.objects.create(**validated_data)
    
#     def update(self, employee, validated_data):
#          newEmployee=Employee(**validated_data)
#          newEmployee.id=employee.id;
#          newEmployee.save()
#          return newEmployee


class Employeeserializer(serializers.ModelSerializer):
   class Meta:
     model=Employee
     fields ='__all__'
    #  fields =['name','email', 'phone']
     

class Userserializer(serializers.Serializer):
    username= serializers.CharField(max_length=40)
    email=   serializers.EmailField( ) 
    password= serializers.CharField(max_length=40)
    
    