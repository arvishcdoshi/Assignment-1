from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'message':'AUTHENTICATED..its working!'}
        return Response(content)
