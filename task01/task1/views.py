from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            count = MyModel.objects.count()
            return Response({
                'message': 'Data saved successfully!',
                'data': serializer.data,
                'count': count
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
