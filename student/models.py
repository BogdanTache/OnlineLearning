from django.db import models

gender_options = [
    ('male', 'Male'),
    ('female', 'Female'),
]

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=gender_options, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
