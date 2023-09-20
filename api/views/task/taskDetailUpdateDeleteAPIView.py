from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Task
from api.serializers import TaskSerializer
from drf_yasg.utils import swagger_auto_schema


class TaskDetailUpdateDeleteAPIView(APIView):
    """
    API View to handle the retrieval, updating, and deletion of Task records.
    """

    @swagger_auto_schema(
        operation_description="Retrieve a Task record by its ID.",
        responses={200: TaskSerializer, 404: "Not Found"},
    )
    def get(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update a Task record by its ID.",
        request_body=TaskSerializer,
        responses={200: TaskSerializer, 400: "Bad Request"},
    )
    def put(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Task record by its ID.",
        responses={204: "No Content", 404: "Not Found"},
    )
    def delete(self, request, id):
        task = self.get_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
