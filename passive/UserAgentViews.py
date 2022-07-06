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
            queryset = UserTable.objects.filter(user_type=request.data.get('user_type'))
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
