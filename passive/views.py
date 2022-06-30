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

@api_view()
def uploadCms(request):
    # queryset = HomeCms.objects.all()
    serializer_class = HomeSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response({
            'status': 200,
            'data': serializer_class.data
        })
    else:
        return Response({
            'status': 200,
            'data': serializer_class.errors
        })


class UploadHomeCms(viewsets.ModelViewSet):
    parser_classes = (JSONParser, MultiPartParser)

    # @action(detail=True, methods=['patch'])
