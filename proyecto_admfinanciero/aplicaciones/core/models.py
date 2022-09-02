from django.db import models

class Linea(models.Model):
    descripcion=models.CharField(verbose_name="Descripcion", max_length=100,unique=True)
    imagen=models.FileField("Foto",upload_to="core/linea", blank=True,null=True)
    estado=models.BooleanField(default=True)
    class Meta:
        verbose_name="Linea producto"
        verbose_name_plural="Lineas productos"
        ordering=("-descripcion",)


    def __str__(self):
        return "{}-{}".format(self.id, self.descripcion)


class Grupo(models.Model):
    linea= models.ForeignKey(Linea,on_delete=models.PROTECT,blank=True,null=True)
    imagen=models.FileField("Foto",upload_to="core/grupo", blank=True,null=True)

    descripcion = models.CharField(max_length=100, unique=True)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name="Categoria producto"
        verbose_name_plural="Categorias productos"
        ordering=("-descripcion",)

    def __str__(self):
        return "{}".format(self.descripcion)