from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Task
from api.serializers import TaskSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class StudentTaskListAPIView(APIView):
    """
    API View to list all Task records associated with a specific student.

    Methods:
    - get(request, student_id) -> Response: List all Task records associated with the student_id.

    """

    @swagger_auto_schema(
        operation_description="List all Task records associated with a specific student.",
        manual_parameters=[
            openapi.Parameter(
                "student_id",
                in_=openapi.IN_PATH,
                description="ID of the student whose tasks are to be listed.",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={
            200: TaskSerializer(many=True),
            204: "No Content: No tasks available for this student.",
            404: "Not Found: The student could not be located.",
        },
    )
    def get(self, request, student_id):
        """
        Handle GET request to list all Task records associated with a specific student.
        ---
        Retrieves all Task records for the student with the given student_id.
        """
        tasks = Task.objects.filter(student_id=student_id)
        if not tasks:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
