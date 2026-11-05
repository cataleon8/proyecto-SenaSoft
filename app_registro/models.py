from django.db import models

class Competidor(models.Model):
    nombre = models.CharField(max_length=100)
    centro = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
