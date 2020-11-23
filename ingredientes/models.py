from django.db import models

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    preparacion = models.TextField()
    ingrediente = models.ForeignKey(
    Ingrediente, related_name="ingredientes", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo
