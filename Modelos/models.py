from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    tipo_funcionario=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    sexo=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    tipo_usuario=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    registrar=models.CharField(max_length=50)
    editar=models.CharField(max_length=50)
    id_funcionario=models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.tipo_usuario  

class Ingreso(models.Model):
    fecha_ingreso=models.DateField(max_length=50)
    fecha_salida=models.DateField(max_length=50)
    estado=models.CharField(max_length=50)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha_ingreso)

class Bitacora(models.Model):
    operacion=models.CharField(max_length=50)
    tabla=models.CharField(max_length=50)
    fecha=models.DateField(max_length=50)
    sintaxis_sql=models.CharField(max_length=50)
    nombre_sql=models.CharField(max_length=50)
    tipo_sql = models.CharField(max_length=50)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.operacion        