from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AdminDataTable
from .seiralizers import AdminSerializer, AdminRegistrationSerializet
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser, FileUploadParser
from .consts import *

class AdminViews(APIView):
    parser_classes = (FormParser, JSONParser,
                      MultiPartParser, FileUploadParser)

    def get(self, request):
        todo_objs = AdminDataTable.objects.all()
        serializer = AdminSerializer(todo_objs, many=True)

        return Response({
            'status': consts.Success,
            'message': ' Retrived Successfully',
            'data': serializer.data
        })

    def post(self, request):
        try:
            data = request.data

            serializer = AdminSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': consts.Success,
                    'message': 'Data Created Successfully',
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
                'message': 'Something went wrong'
            })

    def patch(self, request):
        try:
            data = request.data
            if not data.get('uuid'):
                return Response({
                    'status': consts.Error,
                    'message': 'id is required',
                    'data': {}
                })
            obj = AdminDataTable.objects.get(uuid=data.get('uuid'))
            serializer = AdminSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': consts.Success,
                    'message': ' Updated Successfully',
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
                'message': 'Something went wrong'
            })

