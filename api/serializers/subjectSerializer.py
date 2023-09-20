from rest_framework import serializers
from api.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Subject model, includes all fields.
    """

    class Meta:
        model = Subject
        fields = "__all__"
