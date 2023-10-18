from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from testapp.serializers import MessageSerializer


class CreateMessageAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        text = request.data
        serializer = MessageSerializer(data=text)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
