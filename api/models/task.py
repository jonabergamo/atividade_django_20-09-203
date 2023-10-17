from django.db import models


class Task(models.Model):
    """
    Task model with various fields and foreign key relations to Student and Subject.
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    # Foreign Key and Many-to-Many relations
    student = models.ForeignKey(
        "Student", related_name="tasks", on_delete=models.CASCADE
    )
    subjects = models.ManyToManyField("Subject", related_name="tasks")

    def __str__(self):
        return self.title
