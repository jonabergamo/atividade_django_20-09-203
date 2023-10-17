from django.db import models


class Subject(models.Model):
    """
    Subject model with name and description fields.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
