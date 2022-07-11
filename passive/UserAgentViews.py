from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser, FileUploadParser
from rest_framework.response import Response
from django.core.paginator import  Paginator,EmptyPage
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
            # pdb.set_trace()
            queryset = UserTable.objects.filter(user_type=request.data.get('user_type')).order_by('-id').values()
            # serializer = UserSerializer(queryset, many=True)
            paginator = Paginator(queryset,2)
            page_number = request.GET.get('page')
            try:
                data_final = paginator.get_page(page_number)
            except EmptyPage:
                data_final = paginator.get_page(1)
            serializer = UserSerializer(data_final,many=True)

            pre_page=0
            if data_final.has_previous():
                pre_page = data_final.previous_page_number()

            pagination = {'current_page': page_number,
                          'next_page': data_final.next_page_number(),
                          'previous_page': pre_page,
                          'is_next_page' : data_final.has_next(),
                          'total_entries': queryset.count()}

            data_val={}
            data_val['pagination'] = pagination
            data_val['data'] = serializer.data


            if queryset.exists():
                return Response({
                    'status': consts.Success,
                    'message': 'Retrived',
                    'data': data_val
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
