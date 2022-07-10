from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser, FileUploadParser
from rest_framework.response import Response

from .models import HomeCmsClientsSlider
from .seiralizers import TestimonialSerializer
from .consts import *
import pdb


class TestimonailViews(viewsets.ModelViewSet):
    parser_classes = (FormParser, JSONParser, MultiPartParser, FileUploadParser)

    serializer_class = TestimonialSerializer
    queryset = HomeCmsClientsSlider.objects.all()

    def create(self, request, *args, **kwargs):
        # pdb.set_trace()
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': consts.Success,
                'message': 'Created',
                'data': serializer.data
            })
        return Response({
            'status': consts.Error,
            'error': 'Something went wrong'
        })

    def list(self, request):
        # pdb.set_trace()
        queryset = HomeCmsClientsSlider.objects.all().order_by('-id')
        serializer = TestimonialSerializer(queryset, many=True)
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

    @action(detail=False, methods=['post'])
    def update_testimonial(self, request):
        data = request.data
        try:
            if not data.get('uuid'):
                return Response({
                    'status': consts.Error,
                    'message': 'uuid is required'
                })
            obj = HomeCmsClientsSlider.objects.get(uuid=data.get('uuid'))
            serializer = TestimonialSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': consts.Success,
                    'message': 'Testimonial Updated Successfully',
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
    def get_user_testimonial(self, request):
        try:
            data = request.data
            # pdb.set_trace()
            if not data.get('uuid'):
                return Response({
                    'status': consts.Error,
                    'message': 'uuid is required'
                })

            user = HomeCmsClientsSlider.objects.get(uuid=data.get('uuid'))
            serializer = TestimonialSerializer(user)

            return Response({
                'status': consts.Success,
                'message': 'Testimonial retrived Successfully',
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': consts.Error,
                'message': 'Error',
                'error': str(e)
            })

    # @action(detail=False, methods=['post'])
    # def delete_testimonial(self, request):
    #     try:
    #         # pdb.set_trace()
    #         uuid = request.data.get('uuid')
    #         if not uuid:
    #             return Response({
    #                 'status': consts.Error,
    #                 'message': 'uuid is required'
    #             })
    #         user = HomeCmsClientsSlider.objects.get(uuid=request.data.get('uuid'))
    #         user.delete()
    #         return Response({
    #             'status': consts.Success,
    #             'message': 'Testimonial Deleted Successfully',
    #
    #         })
    #
    #     except Exception as e:
    #         return Response({
    #             'status': consts.Error,
    #             'message': 'Error',
    #             'error': str(e)
    #         })


