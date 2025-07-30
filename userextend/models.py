from django.contrib.auth.models import User
from django.db import models


TYPE_OPTIONS = (
('student', 'student'),
('instructor', 'instructor'),
)

class UserExtend(User):
    type = models.CharField(max_length=15, choices=TYPE_OPTIONS)
