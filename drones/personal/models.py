from django.db import models
"""
from django.contrib.auth.models import AbstractUser,Group,Permission

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=100)



class CustomUser(AbstractUser):
    # autres champs personnalisés ici
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # ajout de related_name
        related_query_name='user'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # ajout de related_name
        related_query_name='user'
    )


from django.db import models

PRIORITY = [
    ("H","High"),
    ("M","Medium"),
    ("L","Low"),
]

class Question(models.Model):
    title      = models.CharField(max_length=60)
    question   = models.TextField(max_length=400) 
    priority   = models.CharField(max_length=1,choices=PRIORITY)
    def _str_(self):
        return self.title
    class Meta:
        verbose_name = "The Question"
        verbose_name_plural = "Peoples Questions"
          """