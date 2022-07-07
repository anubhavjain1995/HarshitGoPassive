from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser, FileUploadParser
from rest_framework.response import Response

from .models import UserTable
from .seiralizers import UserSerializer
from .consts import *
import pdb


class UserAgentViews(viewsets.ModelViewSet):
    parser_classes = (FormParser, JSONParser, MultiPartParser, FileUploadParser)

    serializer_class = UserSerializer
    queryset = UserTable.objects.all()

    @action(detail=False, methods=['post'])
    def get_user_agents(self, request):
        try:
            queryset = UserTable.objects.filter(user_type=request.data.get('user_type')).order_by('-id')
            serializer = UserSerializer(queryset, many=True)
            if queryset.exists():
                return Response({
                    'status': consts.Success,
                    'message': 'Retrived',
                    'data': serializer.data
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
                    'data': str(e)
                })

    @action(detail=False, methods=['post'])
    def update_user_agent(self, request):
        data = request.data
        try:
            if not data.get('uuid'):
                return Response({
                    'status': consts.Error,
                    'message': 'uuid is required'
                })
            obj = UserTable.objects.get(uuid=data.get('uuid'))
            serializer = UserSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': consts.Success,
                    'message': 'User Updated Successfully',
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

    @action(detail=False, methods=['post'])
    def get_user_agent_detail(self, request):
        try:
            data = request.data
            # pdb.set_trace()
            if not data.get('uuid'):
                return Response({
                    'status': consts.Error,
                    'message': 'uuid is required'
                })

            user = UserTable.objects.get(uuid=data.get('uuid'))
            serializer = UserSerializer(user)

            return Response({
                'status': consts.Success,
                'message': 'User retrived Successfully',
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'error': str(e)
            })
