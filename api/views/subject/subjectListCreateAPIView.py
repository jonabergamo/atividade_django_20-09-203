from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Subject
from api.serializers import SubjectSerializer
from drf_yasg.utils import swagger_auto_schema


class SubjectListCreateAPIView(APIView):
    """
    API View to handle the listing and creation of Subject records.

    Methods:
    - get(request) -> Response: Retrieve a list of all Subject records.
    - post(request) -> Response: Create a new Subject record.
    """

    @swagger_auto_schema(
        operation_description="List all Subject records.",
        responses={
            200: SubjectSerializer(many=True),
            204: "No Content: No subjects available.",
        },
    )
    def get(self, request):
        subjects = Subject.objects.all()
        if not subjects:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Subject record.",
        request_body=SubjectSerializer,
        responses={201: SubjectSerializer, 400: "Bad Request: Invalid data."},
    )
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
