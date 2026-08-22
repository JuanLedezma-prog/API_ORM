from rest_framework import serializers

# Create your models here.
class FuncionarioEntrada(serializers.Serializer):
    nombre=serializers.CharField(max_length=50)
    apellido=serializers.CharField(max_length=50)
    tipo_funcionario=serializers.CharField(max_length=50)
    telefono=serializers.CharField(max_length=50)
    correo=serializers.CharField(max_length=50)
    direccion=serializers.CharField(max_length=50)
    sexo=serializers.CharField(max_length=50)



class UsuarioEntrada(serializers.Serializer):
    tipo_usuario=serializers.CharField(max_length=50)
    contraseña=serializers.CharField(max_length=50)
    estado=serializers.CharField(max_length=50)
    registrar=serializers.CharField(max_length=50)
    editar=serializers.CharField(max_length=50)
    id_funcionario=serializers.IntegerField()

class IngresoEntrada(serializers.Serializer):
    fecha_ingreso=serializers.DateField()
    fecha_salida=serializers.DateField()
    estado=serializers.CharField(max_length=50)
    id_usuario=serializers.IntegerField()
    
    

    

class BitacoraEntrada(serializers.Serializer):
    operacion=serializers.CharField(max_length=50)
    tabla=serializers.CharField(max_length=50)
    fecha=serializers.DateField()
    sintaxis_sql=serializers.CharField(max_length=50)
    nombre_sql=serializers.CharField(max_length=50)
    tipo_sql=serializers.CharField(max_length=50)
    id_usuario=serializers.IntegerField()

class MensajeSalida(serializers.Serializer):
    mensaje= serializers.CharField(max_length=100)    
    