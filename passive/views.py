from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status, viewsets, request
from .models import HomeCms, AdminDataTable
from django.contrib.auth import authenticate
from .seiralizers import HomeSerializer, AdminRegistrationSerializet, AdminLoginSerializer, AdminSerializer
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


@api_view(['POST', ])
def adminLogin(request):
    try:
        if request.method == 'POST':
            # pdb.set_trace()

            data = request.data
            if not data.get('email') == "":
                if not data.get('password') == "":
                    # obj = AdminDataTable.objects.get(email=data.get('email'))
                    serializer = AdminLoginSerializer(data=request.data)
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
            'status': 400,
            'message': 'Error',
            'data': 'User doesn\'t exists'
        })


@api_view(['POST', ])
def admin_change_password(request):
    try:
        data = request.data
        # pdb.set_trace()
        if not data.get('uuid'):
            return Response({
                'status': False,
                'message': 'user_id is required',
                'data': {}
            })
        if not data.get('old_password'):
            return Response({
                'status': False,
                'message': 'Old Password is required'
            })
        obj = AdminDataTable.objects.get(uuid=data.get('uuid'))
        serializer = AdminSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            oldpass = obj.password
            newpass = data.get('password')
            if data.get('old_password') == oldpass:
                if oldpass == newpass:
                    return Response({
                        'status': False,
                        'message': 'Error',
                        'error': 'Old and new passwords are same'
                    })
                else:
                    serializer.save()
                    return Response({
                        'status': True,
                        'message': 'Password Changed Successfully'
                    })
        return Response({
            'status': False,
            'message': 'Error',
            'error': serializer.errors
        })
    except Exception as e:
        return Response({
            'status': False,
            'message': 'Something went wrong'
        })


@api_view(['POST', ])
def admin_profile(request):
    if request.method == 'POST':
        todo_objs = AdminDataTable.objects.get(uuid=request.data.get('uuid'))
        serializer = AdminSerializer(todo_objs)

        return Response({
            'status': 200,
            'message': ' Retrived Successfully',
            'data': serializer.data
        })
    else:
        return Response({
            'status': 400,
            'message': 'Error',
            'data': 'Method Not allowed'
        })


@api_view(['POST', ])
def delete_user(request):
    if request.method == 'POST':
        user = AdminDataTable.objects.get(uuid=request.data.get('uuid'))
        user.delete()
        return Response({
            'status': True,
            'message': 'User Deleted'

        })
