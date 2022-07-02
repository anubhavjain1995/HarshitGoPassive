from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AdminDataTable
from .seiralizers import AdminSerializer, AdminRegistrationSerializet
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser, FileUploadParser


class AdminViews(APIView):
    parser_classes = (FormParser, JSONParser,
                      MultiPartParser, FileUploadParser)

    def get(self, request):
        todo_objs = AdminDataTable.objects.all()
        serializer = AdminSerializer(todo_objs, many=True)

        return Response({
            'status': 200,
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
            if not data.get('uuid'):
                return Response({
                    'status': False,
                    'message': 'id is required',
                    'data': {}
                })
            obj = AdminDataTable.objects.get(uuid=data.get('uuid'))
            serializer = AdminSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': ' Updated Successfully',
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

