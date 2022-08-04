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
            paginator = Paginator(queryset,10)

            if request.GET.get('page'):
                page_number = request.GET.get('page')
            else:
                page_number = 1


            if int(page_number) > paginator.num_pages:
                raise ValidationError("Not enough pages", code=404)
            try:
                datafinal = paginator.get_page(page_number)
            except EmptyPage:
                datafinal = paginator.get_page(1)

            serializer = UserLeadsSerializer(datafinal, many=True)


            if queryset.exists():
                return Response({
                    'status': consts.Success,
                    'message': 'Retrived',
                    'data': consts.paginate(serializer.data,paginator,page_number)
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


