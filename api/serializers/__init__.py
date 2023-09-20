"""This package consolidates all serializers used in the application.

Modules:
- TaskSerializer: Serializes the Task model to JSON and validates incoming JSON payloads for tasks.
- StudentSerializer: Serializes the Student model to JSON and validates incoming JSON payloads for students.
- SubjectSerializer: Serializes the Subject model to JSON and validates incoming JSON payloads for subjects.

Each serializer is responsible for converting model instances to JSON
and vice versa, ensuring that the data adheres to predefined schemas.
"""

from .taskSerializer import TaskSerializer
from .studentSerializer import StudentSerializer
from .subjectSerializer import SubjectSerializer
