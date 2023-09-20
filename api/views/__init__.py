"""
API Views Initialization File

This module is responsible for importing all the API views, organized by their respective functionalities.
Each set of views is isolated in its own directory and file to make the project more maintainable and clean.

Structure:

- student: Views related to the Student model
    - StudentDetailUpdateDeleteAPIView: Handles the GET, PUT, and DELETE operations for a single student.
    - StudentListCreateAPIView: Handles the GET and POST operations for the student list.

- subject: Views related to the Subject model
    - SubjectDetailUpdateDeleteAPIView: Handles the GET, PUT, and DELETE operations for a single subject.
    - SubjectListCreateAPIView: Handles the GET and POST operations for the subject list.

- task: Views related to the Task model
    - TaskDetailUpdateDeleteAPIView: Handles the GET, PUT, and DELETE operations for a single task.
    - TaskListCreateAPIView: Handles the GET and POST operations for the task list.

- student_task: Views related to tasks assigned to a specific student
    - StudentTaskListAPIView: Handles the GET operation to list all tasks for a specific student.

"""

from .student.studentDetailUpdateDeleteAPIView import StudentDetailUpdateDeleteAPIView
from .student.studentListCreateAPIView import StudentListCreateAPIView

from .subject.subjectDetailUpdateDeleteAPIView import SubjectDetailUpdateDeleteAPIView
from .subject.subjectListCreateAPIView import SubjectListCreateAPIView

from .task.taskDetailUpdateDeleteAPIView import TaskDetailUpdateDeleteAPIView
from .task.taskListCreateAPIView import TaskListCreateAPIView

from .student_task.studentTaskListAPIView import StudentTaskListAPIView
