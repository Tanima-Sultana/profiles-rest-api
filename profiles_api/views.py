from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class HelloApiView(APIView):
    """Test api view."""

    def get(self, request, format=None):
        """ Returns a list of APIViews features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over you application logic',
        'Its mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
