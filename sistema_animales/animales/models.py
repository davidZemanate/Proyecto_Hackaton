from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Animal Nombre")
    edad = models.CharField(max_length=45, null=True)  
    tipo = models.CharField(max_length=45, verbose_name="Animal Tipo")  
    municipio = models.CharField(max_length=45) 
    departamento = models.CharField(max_length=45)  
    direccion = models.CharField(max_length=45) 
    TIPO_VULNERABILIDAD = [
        ('Abandono', 'Abandono'),
        ('Enfermedad', 'Enfermedad'),
        ('Maltrato', 'Maltrato'),
    ]
    tipo_vulnerabilidad = models.CharField(max_length=45, choices=TIPO_VULNERABILIDAD)
    ayuda_requerida = models.CharField(max_length=45) 
    estado = models.TextField(null=True) 
    fecha_registro = models.DateTimeField(null=True)
    descripcion = models.CharField(max_length=100, null=True)  
    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=45, verbose_name="Persona Nombre")
    telefono_contacto = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre


class Rol(models.Model):
    tipo = models.CharField(max_length=45, verbose_name="Rol Tipo")

    def __str__(self):
        return self.tipo


class Usuario(models.Model):
    username = models.CharField(max_length=45, verbose_name="Usuario")
    contrasena = models.CharField(max_length=45)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Ayuda_Animal(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=45, null=True)
    descripcion = models.CharField(max_length=45, null=True)

    def __str__(self):
        return f"Ayuda para {self.animal.nombre} por {self.usuario.nombre}"
