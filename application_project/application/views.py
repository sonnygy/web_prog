from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApplicationSerializer

class ApplicationCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Заявка успешно отправлена!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)