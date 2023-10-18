from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Student, Subject, Task
from api.serializers import StudentSerializer, SubjectSerializer, TaskSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions


class StudentListCreateAPIView(APIView):
    """
    API View to handle the List and Create operations for the Student model.

    Methods:
    - get(request) -> Response: List all the Student records.
    - post(request) -> Response: Create a new Student record.

    """
    permission_classes=[permissions.IsAuthenticated]
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permission() for permission in self.permission_classes]

    @swagger_auto_schema(
        operation_description="List all Student records.",
        responses={
            200: StudentSerializer(many=True),
            204: "No Content: No students available.",
        },
    )
    def get(self, request):
        """
        Handle GET request to list all Student records.
        ---
        Retrieves all Student records from the database.
        """
        students = Student.objects.all()
        if not students:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Student record.",
        request_body=StudentSerializer,
        responses={
            201: StudentSerializer,
            400: "Bad Request: The request could not be completed due to bad syntax.",
        },
    )
    def post(self, request):
        """
        Handle POST request to create a new Student record.
        ---
        Creates a new Student record and saves it to the database.
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
