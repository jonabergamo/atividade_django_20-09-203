from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404


class StudentDetailUpdateDeleteAPIView(APIView):
    """
    API View to handle CRUD operations for a single Student record.
    """

    @swagger_auto_schema(
        responses={
            200: "OK: Success!",
            404: "Not Found: The student could not be located.",
        },
        operation_description="Retrieve a single Student by their ID.",
    )
    def get(self, request, id):
        """
        Retrieve a Student by ID.
        ---
        Get the Student record matching the given ID.
        """
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=StudentSerializer,
        responses={
            200: "OK: Student updated successfully.",
            400: "Bad Request: The request could not be completed due to bad syntax.",
            404: "Not Found: The student could not be located.",
        },
        operation_description="Update a Student by their ID.",
    )
    def put(self, request, id):
        """
        Update a Student by ID.
        ---
        Update the Student record matching the given ID.
        """
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            204: "No Content: The student was successfully deleted.",
            404: "Not Found: The student could not be located.",
        },
        operation_description="Delete a Student by their ID.",
    )
    def delete(self, request, id):
        """
        Delete a Student by ID.
        ---
        Remove the Student record matching the given ID.
        """
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        """
        Retrieve the Student object using the given ID.
        """
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404("Student does not exist")
