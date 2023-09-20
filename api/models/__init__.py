"""This package handles the core domain logic for the application.

Modules:
- Student: Manages the Student model and its associated functionalities.
- Subject: Manages the Subject model and related operations.
- Task: Manages the Task model and relevant functionalities.

Each module is designed to operate independently but can be used together
to create complex workflows.
"""

from .student import Student
from .subject import Subject
from .task import Task
