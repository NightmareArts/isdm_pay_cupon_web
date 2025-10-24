from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        PROGRAMMER = "PROGRAMMER", "Programador"
        STUDENT    = "STUDENT", "Alumno"
        ADMIN      = "ADMIN", "Administrativo"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.STUDENT)

    def is_programmer(self): return self.role == self.Roles.PROGRAMMER
    def is_student(self):    return self.role == self.Roles.STUDENT
    def is_admin_staff(self):return self.role == self.Roles.ADMIN
