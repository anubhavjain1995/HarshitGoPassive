from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status, viewsets, request
from .models import HomeCms, AdminDataTable, UserTable,HomeCmsClientsSlider
from django.contrib.auth import authenticate
from .seiralizers import HomeSerializer, AdminRegistrationSerializet, AdminLoginSerializer, AdminSerializer, \
    UserSerializer, UserRegistrationSerializer, UserLoginSerializer
from .consts import *


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
            'status': consts.Success,
            'data': serializer_class.data
        })
    else:
        return Response({
            'status': consts.Error,
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
                    'status': consts.Success,
                    'message': 'User Created Successfully',
                    'data': serializer.data
                })
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'data': serializer.errors
            })
    except Exception as e:
        print('%s' % type(e))
        return Response({
            'status': consts.Error,
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
                            'status': consts.Success,
                            'message': 'Login Successfully',
                            'data': serializer.data
                        })
                    return Response({
                        'status': consts.Error,
                        'message': 'Something went wrong',
                        'data': serializer.errors
                    })
                return Response({
                    'status': consts.Error,
                    'message': 'Error',
                    'data': {'password': 'password doesn\'t matches'}
                })
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'data': {'email': 'User doesn\'t exists'}
            })

    except Exception as e:
        print('%s' % type(e))
        return Response({
            'status': consts.Error,
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
                'status': consts.Error,
                'message': 'user_id is required',
                'data': {}
            })
        if not data.get('old_password'):
            return Response({
                'status': consts.Error,
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
                        'status': consts.Error,
                        'message': 'Error',
                        'error': 'Old and new passwords are same'
                    })
                else:
                    serializer.save()
                    return Response({
                        'status': consts.Success,
                        'message': 'Password Changed Successfully'
                    })
        return Response({
            'status': consts.Error,
            'message': 'Error',
            'error': serializer.errors
        })
    except Exception as e:
        return Response({
            'status': consts.Error,
            'message': 'Something went wrong'
        })


@api_view(['GET', ])
def admin_profile(request,pk):
    if request.method == 'GET':
        todo_objs = AdminDataTable.objects.get(uuid=pk)
        serializer = AdminSerializer(todo_objs,many=False)

        return Response({
            'status': consts.Success,
            'message': ' Retrived Successfully',
            'data': serializer.data
        })
    else:
        return Response({
            'status': consts.Error,
            'message': 'Error',
            'data': 'Method Not allowed'
        })


@api_view(['DELETE', ])
def delete_user(request,pk):
    if request.method == 'DELETE':
        user = AdminDataTable.objects.get(uuid=pk)
        user.delete()
        return Response({
            'status': consts.Success,
            'message': 'User Deleted'

        })


# Agent and User Registration

@api_view(['POST', ])
def user_registration(request):
    try:
        if request.method == 'POST':
            # pdb.set_trace()
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': consts.Success,
                    'message': 'User Created Successfully',
                    'data': serializer.data
                })
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'data': serializer.errors
            })
    except Exception as e:
        print('%s' % type(e))
        return Response({
            'status': consts.Error,
            'message': 'Something went wrong'

        })


@api_view(['POST', ])
def userLogin(request):
    try:
        if request.method == 'POST':
            # pdb.set_trace()

            data = request.data
            if not data.get('email') == "":
                if not data.get('password') == "":
                    # obj = AdminDataTable.objects.get(email=data.get('email'))
                    serializer = UserLoginSerializer(data=request.data)
                    if serializer.is_valid():
                        return Response({
                            'status': consts.Success,
                            'message': 'Login Successfully',
                            'data': serializer.data
                        })
                    return Response({
                        'status': consts.Error,
                        'message': 'Something went wrong',
                        'data': serializer.errors
                    })
                return Response({
                    'status': consts.Error,
                    'message': 'Error',
                    'data': {'password': 'password doesn\'t matches'}
                })
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'data': {'email': 'User doesn\'t exists'}
            })

    except Exception as e:
        print('%s' % type(e))
        return Response({
            'status': consts.Error,
            'message': 'Error',
            'data': 'User doesn\'t exists'
        })


@api_view(['POST', ])
def user_change_password(request):
    try:
        data = request.data
        # pdb.set_trace()
        if not data.get('uuid'):
            return Response({
                'status': consts.Error,
                'message': 'user_id is required',
                'data': {}
            })
        if not data.get('old_password'):
            return Response({
                'status': consts.Error,
                'message': 'Old Password is required'
            })
        obj = UserTable.objects.get(uuid=data.get('uuid'))
        serializer = UserSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            oldpass = obj.password
            newpass = data.get('password')
            if data.get('old_password') == oldpass:
                if oldpass == newpass:
                    return Response({
                        'status': consts.Error,
                        'message': 'Error',
                        'error': 'Old and new passwords are same'
                    })
                else:
                    serializer.save()
                    return Response({
                        'status': consts.Success,
                        'message': 'Password Changed Successfully'
                    })
        return Response({
            'status': consts.Error,
            'message': 'Error',
            'error': serializer.errors
        })
    except Exception as e:
        return Response({
            'status': consts.Error,
            'message': 'Something went wrong'
        })


@api_view(['GET', ])
def user_profile(request,pk):
    try:
        if request.method == 'GET':
            todo_objs = UserTable.objects.get(uuid=pk)
            serializer = UserSerializer(todo_objs,many=False)

            return Response({
                'status': consts.Success,
                'message': ' Retrived Successfully',
                'data': serializer.data
            })
        else:
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'data': 'Method Not allowed'
            })
    except Exception as e:
        return Response({
                'status': consts.Error,
                'message': 'Error',
                'data': str(e)
            })


@api_view(['DELETE'],)
def delete_testimonial(request,pk):
    if request.method == 'DELETE':
        user = HomeCmsClientsSlider.objects.get(uuid=pk)
        user.delete()
        return Response({
            'status': consts.Success,
            'message': 'Testimonial Deleted'
        })
