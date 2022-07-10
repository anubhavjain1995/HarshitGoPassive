from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .seiralizers import UserLeadsSerializer
from .models import UserLeadsTable
from .consts import *
import pdb


class LeadsViews(viewsets.ModelViewSet):
    serializer_class = UserLeadsSerializer
    queryset = UserLeadsTable.objects.all()

    def create(self, request, *args, **kwargs):
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
            'error': 'Something went wrong'
        })

    def list(self, request):
        # pdb.set_trace()
        queryset = UserLeadsTable.objects.all().order_by('-id')
        serializer = UserLeadsSerializer(queryset, many=True)
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

