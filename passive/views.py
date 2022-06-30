from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status, viewsets, request
from .models import HomeCms
from .seiralizers import HomeSerializer


# Create your views here.

@api_view()
def home(request):
    return Response({"message": "Hello, world!"})
