from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status,viewsets
# Create your views here.

@api_view()
def home(request):
    return Response({"message": "Hello, world!"})
