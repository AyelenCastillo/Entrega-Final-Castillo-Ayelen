from django.db import models
from django.contrib.auth.models import User

class Postres(models.Model):
    titulo = models.CharField(max_length=100)
    receta = models.TextField()
    ingredientes = models.TextField(default=None)  
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.autor}'

class Comidas(models.Model):
    titulo = models.CharField(max_length=100)
    receta = models.TextField()
    ingredientes = models.TextField(default=None)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.autor}'

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
    