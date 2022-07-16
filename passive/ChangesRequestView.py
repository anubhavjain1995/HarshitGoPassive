from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage
from .seiralizers import ChangesRequestSerializer, UserSerializer
from .models import ChangesRequestTable, UserTable
from .consts import *
import pdb


class ChangesRequestView(viewsets.ModelViewSet):
    serializer_class = ChangesRequestSerializer
    queryset = ChangesRequestTable.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ChangesRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': consts.Success,
                'message': 'Request Submitted',
                'data': serializer.data
            })
        else:
            return Response({
                'status': consts.Error,
                'error': 'Something went wrong'
            })

    def list(self, request):
        # pdb.set_trace()
        try:
            queryset = ChangesRequestTable.objects.all().order_by('-id')
            serializer = ChangesRequestSerializer(queryset, many=True)

            a = []
            user_email = ''
            for i in range(len(serializer.data)):
                uuid = serializer.data[i]['uuid']
                user = UserTable.objects.get(uuid=uuid)
                user_serializer = UserSerializer(user)
                user_email = user_serializer.data.get('email')
                user_name = user_serializer.data.get('username')
                resp = {"email": user_email,
                        "username": user_name,
                        "message": serializer.data[i]['message'],
                        'is_done': serializer.data[i]['is_done'],
                        'created_at': serializer.data[i]['created_at']}
                a.append(resp)
            if queryset.exists():
                return Response({
                    'status': consts.Success,
                    'message': 'Retrived',
                    'data': a
                })
            return Response({
                'status': consts.Success,
                'message': 'No data found',
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'error': type(e)
            })

    @action(detail=False, methods=['patch'])
    def update_request(self, request):
        data = request.data
        try:
            if not data.get('uuid'):
                return Response({
                    'status': consts.Error,
                    'message': 'uuid is required'
                })
            obj = ChangesRequestTable.objects.get(uuid=data.get('uuid'))
            serializer = ChangesRequestSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': consts.Success,
                    'message': 'Updated Successfully',
                    'data': serializer.data
                })
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'error': serializer.errors
            })
        except Exception as e:
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'error': type(e)
            })
