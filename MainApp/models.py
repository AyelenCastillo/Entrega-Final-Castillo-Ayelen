from django.db import models

# Create your models here.

class Postres(models.Model):
    titulo = models.CharField(max_length=40)
    receta =  models.TextField()
    autor = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.titulo} - {self.autor}'


class Comidas(models.Model):
    titulo = models.CharField(max_length=40)
    receta =  models.TextField()
    autor = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.titulo} - {self.autor}'

class Registro(models.Model):
    nombre = models.CharField(max_length=30)
    password = models.CharField(max_length=128, default='password123')
    email= models.EmailField(null=True)

