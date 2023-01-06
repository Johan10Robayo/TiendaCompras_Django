from django.db import models

# Create your models here.

class Cartegoria_prod(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta: #nombres ensingular y plural
        verbose_name="categoria_prod"
        verbose_name_plural="categorias_prod"

    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(Cartegoria_prod,on_delete=models.CASCADE)#relacion de uno a muchos
    imagen=models.ImageField(upload_to="tienda",null=True,blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
