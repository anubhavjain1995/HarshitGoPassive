from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status, viewsets, request
from .models import HomeCms
from .seiralizers import HomeSerializer,AdminRegistrationSerializet,AdminLoginSerializer
import pdb;
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

@api_view(['POST',])
def registration(request):
       try:
           if request.method == 'POST':
               # pdb.set_trace()
               serializer = AdminRegistrationSerializet(data=request.data)
               if serializer.is_valid():
                   serializer.save()
                   return Response({
                       'status': 200,
                       'message': 'User Created Successfully',
                       'data': serializer.data
                   })
               return Response({
                   'status': 400,
                   'message': 'Error',
                   'data': serializer.errors
               })
       except Exception as e:
            print('%s' % type(e))
            return Response({
                'status': False,
                'message': 'Something went wrong'

            })

@api_view(['POST',])
def adminLogin(request):
       try:
           if request.method == 'POST':
               # pdb.set_trace()
               serializer = AdminLoginSerializer(data=request.data)
               if serializer.is_valid():
                   return Response({
                       'status': 200,
                       'message': 'User Created Successfully',
                       'data': serializer.data
                   })
               return Response({
                   'status': 400,
                   'message': 'Error',
                   'data': serializer.errors
               })
       except Exception as e:
            print('%s' % type(e))
            return Response({
                'status': False,
                'message': 'Something went wrong'

            })


class UploadHomeCms(viewsets.ModelViewSet):
    parser_classes = (JSONParser, MultiPartParser)

    # @action(detail=True, methods=['patch'])
