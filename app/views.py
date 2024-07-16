from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from .models import Employee
from .serializer import Employeeserializer ,Userserializer
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet,ModelViewSet

# Create your views here.
class EmployeeViewset(ModelViewSet):
   queryset=Employee.objects.all()
   serializer_class=Employeeserializer   

# -----------ViewSet-------------
# class EmployeeViewset(ViewSet):
#     def list(self,request):
#         employee= Employee.objects.all()
#         serializer= Employeeserializer(employee,many=True)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer= Employeeserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors) 
        
#     def retrieve(self,request,pk):
#         try:
#            employee=Employee.objects.get(pk=pk)
      
#         except Employee.DoesNotExist:
           
#            return Response(status=404)
#         serializer= Employeeserializer(employee)
#         return Response(serializer.data)
         
# -------------------generic view------------------
# class employeeListview(generics.ListAPIView,generics.CreateAPIView):
#    queryset=Employee.objects.all()
#    serializer_class=Employeeserializer

# class employeeListview(generics.ListCreateAPIView):
#    queryset=Employee.objects.all()
#    serializer_class=Employeeserializer

# class employeedetailview(generics.CreateAPIView,generics.RetrieveAPIView,generics.DestroyAPIView):
#    queryset=Employee.objects.all()
#    serializer_class=Employeeserializer

# class employeedetailview(generics.RetrieveUpdateDestroyAPIView):
#    queryset=Employee.objects.all()
#    serializer_class=Employeeserializer





# --------mixin method----------
# class employeeListview(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#    queryset=Employee.objects.all()
#    serializer_class=Employeeserializer
#    def get(self,request):
#       return self.list(request)
#    def post(self,request):
#       return self.create(request)

# class employeedetailview(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#    queryset=Employee.objects.all()
#    serializer_class=Employeeserializer   
#    def get(self,request,pk):
#       return self.retrieve(request,pk)
#    def put(self,request,pk):
#       return self.update(request,pk)
#    def delete(self,request,pk):
#       return self.destroy(request,pk)



# # ---------------class based view----------------

# class employeeListview(APIView):
#     def get(self,request):
#         employee= Employee.objects.all()
#         serializer= Employeeserializer(employee,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer= Employeeserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors) 
        


# class employeedetailview(APIView):
#     def get_employee(self,pk):
#       try:
#         return Employee.objects.get(pk=pk)
      
#       except Employee.DoesNotExist:
#          return Response(status=404)
        
#     def get(self,request,pk):
#       employee=self.get_employee(pk)
#       serializer= Employeeserializer(employee)
#       return Response( serializer.data )
#     def delete(self,request,pk):
#        employee=self.get_employee(pk)
#        employee.delete()
#        return Response(status= status.HTTP_204_NO_CONTENT)
#     def put(self,request,pk):
#        employee=self.get_employee(pk)
#        serializer=Employeeserializer(employee,data=request.data)
#        if serializer.is_valid():
#          serializer.save()
#          return Response( serializer.data )
#        else:
#          return Response(serializer.errors )
       
# ----------------Function based views----------------
# @api_view(['GET' , 'POST'])
# def employeeListview(request):
#     if request.method =='GET':
#       employees = Employee.objects.all()
#       serializer = Employeeserializer(employees , many=True)
#       return Response( serializer.data )
    
#     elif request.method =='POST':
#       serializer=Employeeserializer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response( serializer.data  )
#       else:
#          return Response(serializer.errors )
      
# @api_view(['DELETE' , 'GET','PUT'])    
# def employeedetailview(request,pk):
#    try:
#       employee=Employee.objects.get(pk=pk)
      
#    except Employee.DoesNotExist:
#       return Response(status=404)
#    if request.method=='DELETE':
#        employee.delete()
#        return Response(status= status.HTTP_204_NO_CONTENT)
#    elif request.method=='GET':
#       serializer= Employeeserializer(employee)
#       return Response( serializer.data )
#    elif request.method =='PUT':
#        serializer=Employeeserializer(employee,data=request.data)
#        if serializer.is_valid():
#          serializer.save()
#          return Response( serializer.data )
#        else:
#          return Response(serializer.errors )

# @api_view(['GET'])
# def UserListView(request):
#     if request.method=='GET':
#      users= User.objects.all()
#      serializer =Userserializer(users,many= True)
#      return Response(serializer.data )