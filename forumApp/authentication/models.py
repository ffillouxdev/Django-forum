from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    PROFESSOR = 'professor'
    STUDENT = 'student'
    IT = 'IT license'
    MATH = 'MATH license'
    PHYS = 'PHYS license'
    Medecine = 'Medecine'
    Sociology = 'Sociology license'

    ROLE_CHOICES = [
        (PROFESSOR, 'Professor'),
        (STUDENT, 'Student'),
    ]
    
    STUDIES_CHOICES = [
        (IT, 'IT license'),
        (MATH, 'MATH license'),
        (PHYS, 'PHYS license'),
        (Medecine, 'Medecine'),
        (Sociology, 'Sociology license'),
    ]
    

    profile_picture = models.ImageField(verbose_name='profile_picture', blank=True, null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    studies = models.CharField(max_length=30, choices=STUDIES_CHOICES, verbose_name='Studies', default='')
    