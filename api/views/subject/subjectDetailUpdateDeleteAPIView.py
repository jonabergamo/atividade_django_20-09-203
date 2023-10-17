from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Subject
from api.serializers import SubjectSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated



class SubjectDetailUpdateDeleteAPIView(APIView):
    """
    API View to manage CRUD operations for a specific Subject record.

    Methods:
    - get(request, id) -> Response: Retrieve a Subject record by ID.
    - put(request, id) -> Response: Update a Subject record by ID.
    - delete(request, id) -> Response: Delete a Subject record by ID.
    """
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a specific Subject by ID.",
        responses={200: SubjectSerializer, 404: "Not Found: Subject does not exist."},
    )
    def get(self, request, id):
        subject = self.get_object(id)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=SubjectSerializer,
        operation_description="Update a specific Subject by ID.",
        responses={
            200: SubjectSerializer,
            400: "Bad Request: Invalid data.",
            404: "Not Found: Subject does not exist.",
        },
    )
    def put(self, request, id):
        subject = self.get_object(id)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a specific Subject by ID.",
        responses={
            204: "No Content: Deletion successful.",
            404: "Not Found: Subject does not exist.",
        },
    )
    def delete(self, request, id):
        subject = self.get_object(id)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        try:
            return Subject.objects.get(id=id)
        except Subject.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
