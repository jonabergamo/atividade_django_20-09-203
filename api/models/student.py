from django.db import models


class Student(models.Model):
    """
    Student model with name and unique email fields.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
