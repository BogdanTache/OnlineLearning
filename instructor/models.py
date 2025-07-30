from django.db import models


class Instructor(models.Model):

    course_option = [
        ('hr', 'Human Resources'),
        ('it', 'Information Technology'),
        ('sales', 'Sales'),
        ('marketing', 'Marketing'),
        ('finance', 'Finance'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    course = models.CharField(max_length=50, choices=course_option)
    active = models.BooleanField(default=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

