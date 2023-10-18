from rest_framework import serializers
from api.models import Student
from django.contrib.auth.hashers import make_password


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for Student model, includes all fields.
    """

    class Meta:
        model = Student
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(StudentSerializer, self).create(validated_data)