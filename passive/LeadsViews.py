from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .seiralizers import UserLeadsSerializer
from .models import UserLeadsTable
from django.core.paginator import Paginator,EmptyPage
from .consts import *
import pdb


class LeadsViews(viewsets.ModelViewSet):
    serializer_class = UserLeadsSerializer
    queryset = UserLeadsTable.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            serializer = UserLeadsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': consts.Success,
                    'message': 'Lead Created',
                    'data': serializer.data
                })
            return Response({
                'status': consts.Error,
                'error': 'Something went wrong',
                'data': serializer.errors
            })

        except Exception as e:
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'data': str(e)
            })

    def list(self, request):
        # pdb.set_trace()
        try:
            queryset = UserLeadsTable.objects.all().order_by('-id')
            paginator = Paginator(queryset,4)
            page_number = request.GET.get('page')
            try:
                datafinal = paginator.get_page(page_number)
            except EmptyPage:
                datafinal = paginator.get_page(1)
            serializer = UserLeadsSerializer(datafinal, many=True)
            pre_page = 0
            if datafinal.has_previous():
                pre_page = datafinal.previous_page_number()
            pagination = {'current_page': page_number,
                          'next_page': datafinal.next_page_number(),
                          'previous_page': pre_page,
                          'is_next_page': datafinal.has_next(),
                          'total_entries': queryset.count()
                          }
            data_val = {}
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


