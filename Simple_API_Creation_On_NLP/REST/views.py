from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from .import spacy_code


global data;
data=[]


class Spacy_part_of_speech(APIView):

    def get(self,request,format='None'):
        datam=request.data
        name=datam.get('data','None')
        name = spacy_code.spacy_fun(name)
        message={
            'Response':200,
            'Message': "GET request success",
            'data':name,
        }
        return Response(message)

    def post(self,request,format=None):
        datam=request.data
        name=datam.get('data',None)
        name=spacy_code.spacy_fun(name)

        message={
            'Response':200,
            'Message': "POST request success",
            'data':name,
        }
        return Response(message)