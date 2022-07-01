from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status, viewsets, request
from .models import HomeCms, AdminModelTable
from .seiralizers import HomeSerializer, AdminRegistrationSerializet, AdminLoginSerializer
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


@api_view(['POST', ])
def registration(request):
    try:
        if request.method == 'POST':
            pdb.set_trace()
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


@api_view(['POST', ])
def adminLogin(request):
    try:
        if request.method == 'POST':
            # pdb.set_trace()

            data = request.data
            if not data.get('email') == "":
                if not data.get('password') == "":
                    obj = AdminModelTable.objects.get(email=data.get('email'),admin_type=2)
                    serializer = AdminLoginSerializer(obj,data=request.data)
                    if serializer.is_valid():
                        return Response({
                            'status': 200,
                            'message': 'Login Successfully',
                            'data': serializer.data
                        })
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': serializer.errors
                    })
                return Response({
                    'status': 400,
                    'message': 'Error',
                    'data': {'password': 'password doesn\'t matches'}
                })
            return Response({
                'status': 400,
                'message': 'Error',
                'data': {'email': 'User doesn\'t exists'}
            })

    except Exception as e:
        print('%s' % type(e))
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })

