from rest_framework import serializers
from api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model, includes all fields.
    """

    class Meta:
        model = Task
        fields = "__all__"
