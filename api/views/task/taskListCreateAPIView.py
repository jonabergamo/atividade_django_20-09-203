from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Task
from api.serializers import TaskSerializer
from drf_yasg.utils import swagger_auto_schema


class TaskListCreateAPIView(APIView):
    """
    API View to handle the retrieval and creation of Task records.
    """

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Task records.",
        responses={200: TaskSerializer(many=True)},
    )
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Task record.",
        request_body=TaskSerializer,
        responses={201: TaskSerializer, 400: "Bad Request"},
    )
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
