from django.shortcuts import render
from .models import UserRegister
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Userserializer

# Create your views here.



@api_view(['GET'])
def user_register(request):
    user = UserRegister.objects.all()
    serializer = Userserializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createuser(request):
    newuser = Userserializer(data=request.data)
    if newuser.is_valid():
        newuser.save()
    return Response(newuser.data)


@api_view(['PUT'])
def update(request,id):
    user = UserRegister.objects.get(id=id)
    newuser = Userserializer(data=request.data, instance=user)
    if newuser.is_valid(raise_exception=True):
        newuser.save()
        return Response(newuser.data)


@api_view(['DELETE'])
def delete(request,id):
    user = UserRegister.objects.get(id=id)
    user.delete()
    return Response("user is deleted")