from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HomeCms
from .seiralizers import HomeSerializer
from rest_framework.parsers import FormParser,JSONParser, MultiPartParser,FileUploadParser


class CmsViews(APIView):
    parser_classes = (FormParser,JSONParser, MultiPartParser,FileUploadParser)

    def get(self, request):
        todo_objs = HomeCms.objects.all()
        serializer = HomeSerializer(todo_objs, many=True)

        return Response({
            'status': 200,
            'message': 'Home Retrived Successfully',
            'data': serializer.data
        })

    def post(self, request):
        try:
            data = request.data

            serializer = HomeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Data Created Successfully',
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
                'message': 'Something went wrong'
            })

    def patch(self, request):
        try:
            data = request.data
            if not data.get('id'):
                return Response({
                    'status': False,
                    'message': 'id is required',
                    'data': {}
                })
            obj = HomeCms.objects.get(id=data.get('id'))
            serializer = HomeSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'HomeCms Updated Successfully',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': 'Error',
                'error': serializer.errors
            })
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Something went wrong'
            })

