from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser, FileUploadParser
from rest_framework.response import Response

from .models import HomeCmsClientsSlider
from .seiralizers import TestimonialSerializer
import pdb


class TestimonailViews(viewsets.ModelViewSet):
    parser_classes = (FormParser, JSONParser, MultiPartParser, FileUploadParser)

    queryset = HomeCmsClientsSlider.objects.all()

    def list(self, request):
        serializer = TestimonialSerializer(self.queryset, many=True)
        if self.queryset.exists():
            return Response({
                'status': 200,
                'message': 'Retrived',
                'data': serializer.data
            })
        return Response({
            'status': 200,
            'message': 'No data found',
            'data': serializer.data
        })


    def update(self, request, *args, **kwargs):
        data = request.data
        try:
            if not data.get('uuid'):
                return Response({
                    'status': 400,
                    'message': 'uuid is required'
                })
            obj = HomeCmsClientsSlider.objects.get(uuid=data.get('uuid'))
            serializer = TestimonialSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Testimonial Updated Successfully',
                    'data': serializer.data
                })
            return Response({
                'status': 400,
                'message': 'Error',
                'error': serializer.errors
            })
        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Error',
                'error': type(e)
            })

    def retrieve(self, request, pk=None):
        try:
            uuid = request.data.get('uuid')
            if not uuid:
                return Response({
                    'status': 400,
                    'message': 'uuid is required'
                })
            user = HomeCmsClientsSlider.objects.get(uuid=uuid)
            serializer = TestimonialSerializer(user)
            return Response({
                'status': 200,
                'message': 'Testimonial retrived Successfully',
                'data': serializer.data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Error',
                'error': str(e)
            })

    def destroy(self, request, *args, **kwargs):
        try:
            # pdb.set_trace()
            uuid = request.data.get('uuid')
            if not uuid:
                return Response({
                    'status': 400,
                    'message': 'uuid is required'
                })
            user = HomeCmsClientsSlider.objects.get(uuid=uuid)
            user.delete()
            return Response({
                'status': 200,
                'message': 'Testimonial Deleted Successfully',

            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Error',
                'error': str(e)
            })
