from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializer import FuncionarioEntrada, UsuarioEntrada, IngresoEntrada, BitacoraEntrada, MensajeSalida
from .models import Funcionario, Usuario, Ingreso, Bitacora

# Create your views here.
class FuncionarioView(APIView):
    @swagger_auto_schema(
        operation_description="Registrar un nuevo funcionario",
        request_body=FuncionarioEntrada,
        responses={200: MensajeSalida})
    
    def post(self, request):
        nombre = request.data.get('nombre')
        apellido = request.data.get('apellido')
        tipo_funcionario = request.data.get('tipo_funcionario')
        telefono = request.data.get('telefono')
        correo = request.data.get('correo')
        direccion = request.data.get('direccion')
        sexo = request.data.get('sexo')
        
        funcionario = Funcionario.objects.create(
            nombre=nombre,
            apellido=apellido,
            tipo_funcionario=tipo_funcionario,
            telefono=telefono,
            correo=correo,
            direccion=direccion,
            sexo=sexo
        )
        return Response({'mensaje': 'Funcionario creado exitosamente.'})
    


    @swagger_auto_schema(
        operation_description="Obtener todos los funcionarios",
    )
    
    def get(self, request):
        funcionarios = Funcionario.objects.all()
        lista = []
        for funcionario in funcionarios:
            lista.append({
                'id': funcionario.id,
                'nombre': funcionario.nombre,
                'apellido': funcionario.apellido,
                'tipo_funcionario': funcionario.tipo_funcionario,
                'telefono': funcionario.telefono,
                'correo': funcionario.correo,
                'direccion': funcionario.direccion,
                'sexo': funcionario.sexo
            })
        return Response(lista)
    
    
class FuncionarioIdView(APIView):
    @swagger_auto_schema(
        operation_description="Actualizar un funcionario por ID",
        request_body=FuncionarioEntrada,
        responses={200: MensajeSalida})

    
    def put(self, request, id):
        funcionario = Funcionario.objects.get(id=id)
        funcionario.nombre = request.data.get('nombre')
        funcionario.apellido = request.data.get('apellido')
        funcionario.tipo_funcionario = request.data.get('tipo_funcionario')
        funcionario.telefono = request.data.get('telefono')
        funcionario.correo = request.data.get('correo')
        funcionario.direccion = request.data.get('direccion')
        funcionario.sexo = request.data.get('sexo')
        funcionario.save()
        return Response({'mensaje': 'Funcionario actualizado exitosamente.'})


    
    @swagger_auto_schema(
        operation_description="Eliminar un funcionario por ID",
        responses={200: MensajeSalida}
    )
    def delete(self, request, id):
        funcionario = Funcionario.objects.get(id=id)
        funcionario.delete()
        return Response({'mensaje': 'Funcionario eliminado exitosamente.'})

############################################################################################
class UsuarioView(APIView):
    @swagger_auto_schema(
        operation_description="Registrar un nuevo usuario",
        request_body=UsuarioEntrada,
        responses={200: MensajeSalida})
    
    def post(self, request):
        tipo_usuario = request.data.get('tipo_usuario')
        contraseña = request.data.get('contraseña')
        estado = request.data.get('estado')
        registrar = request.data.get('registrar')
        editar = request.data.get('editar')
        id_funcionario = request.data.get('id_funcionario')

        usuario = Usuario.objects.create(
            tipo_usuario=tipo_usuario,
            contraseña=contraseña,
            estado=estado,
            registrar=registrar,
            editar=editar,
            id_funcionario_id=id_funcionario
        )
        return Response({'mensaje': 'Usuario creado exitosamente.'})



    @swagger_auto_schema(
        operation_description="Obtener todos los usuarios",
    )
    def get(self, request):
        usuarios = Usuario.objects.all()
        lista = []
        for usuario in usuarios:
            lista.append({
                'id': usuario.id,
                'tipo_usuario': usuario.tipo_usuario,
                'estado': usuario.estado,
                'registrar': usuario.registrar,
                'editar': usuario.editar,
                'id_funcionario': usuario.id_funcionario_id
            })
        return Response(lista)

    

class UsuarioIdView(APIView):
    @swagger_auto_schema(
        operation_description="Actualizar usuario por ID",
        request_body=UsuarioEntrada,
        responses={200: MensajeSalida})
    def put(self, request, id):
        usuario = Usuario.objects.get(id=id)
        usuario.tipo_usuario = request.data.get('tipo_usuario')
        usuario.contraseña = request.data.get('contraseña')
        usuario.estado = request.data.get('estado')
        usuario.registrar = request.data.get('registrar')
        usuario.editar = request.data.get('editar')
        usuario.save()
        return Response({'mensaje': 'Usuario actualizado exitosamente.'})


    @swagger_auto_schema(
        operation_description="Eliminar usuario por ID",
        responses={200: MensajeSalida}
    )
    def delete(self, request, id):
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return Response({'mensaje': 'Usuario eliminado exitosamente.'})

##########################################################

class IngresoView(APIView):
    @swagger_auto_schema(
        operation_description="Registrar un nuevo ingreso",
        request_body=IngresoEntrada,
        responses={200: MensajeSalida})
    
    def post(self, request):
        fecha_ingreso = request.data.get('fecha_ingreso')
        fecha_salida = request.data.get('fecha_salida')
        estado = request.data.get('estado')
        id_usuario = request.data.get('id_usuario')  # el cliente debe enviar este dato

        usuario = Usuario.objects.get(id=id_usuario)

        ingreso = Ingreso.objects.create(
            fecha_ingreso=fecha_ingreso,
            fecha_salida=fecha_salida,
            estado=estado,
            id_usuario=usuario,
        )
        return Response({'mensaje': 'Ingreso registrado exitosamente.'})



    @swagger_auto_schema(
        operation_description="Obtener todos los ingresos",
    )

    def get(self, request):
        ingresos = Ingreso.objects.all()
        lista = []
        for ingreso in ingresos:
            lista.append({
                'id': ingreso.id,
                'fecha_ingreso': ingreso.fecha_ingreso,
                'fecha_salida': ingreso.fecha_salida,
                'estado': ingreso.estado,
                
            })
        return Response(lista)


class IngresoIdView(APIView):
    @swagger_auto_schema(
        operation_description="Actualizar un ingreso por ID",
        request_body=IngresoEntrada,
        responses={200: MensajeSalida})

    
    def put(self, request, id):
        ingreso = Ingreso.objects.get(id=id)
        ingreso.fecha_ingreso = request.data.get('fecha_ingreso')
        ingreso.fecha_salida = request.data.get('fecha_salida')
        ingreso.estado = request.data.get('estado')
        ingreso.save()
        return Response({'mensaje': 'Ingreso actualizado exitosamente.'})

    @swagger_auto_schema(
        operation_description="Eliminar un ingreso por ID",
        responses={200: MensajeSalida}
    )
    def delete(self, request, id):
        ingreso = Ingreso.objects.get(id=id)
        ingreso.delete()
        return Response({'mensaje': 'Ingreso eliminado exitosamente.'})
#########################################################################

class BitacoraView(APIView):
    @swagger_auto_schema(
        operation_description="Registrar una nueva bitácora",
        request_body=BitacoraEntrada,
        responses={200: MensajeSalida})
    
    def post(self, request):
        operacion = request.data.get('operacion')
        tabla = request.data.get('tabla')
        fecha = request.data.get('fecha')
        sintaxis_sql = request.data.get('sintaxis_sql')
        nombre_sql = request.data.get('nombre_sql')
        tipo_sql = request.data.get('tipo_sql')
        id_usuario = request.data.get('id_usuario')

        bitacora = Bitacora.objects.create(
            operacion=operacion,
            tabla=tabla,
            fecha=fecha,
            sintaxis_sql=sintaxis_sql,
            nombre_sql=nombre_sql,
            tipo_sql=tipo_sql,
            id_usuario_id=id_usuario
        )
        return Response({'mensaje': 'Bitácora registrada exitosamente.'})


    @swagger_auto_schema(
        operation_description="Obtener todas las bitácoras",
    )

    def get(self, request):
        bitacoras = Bitacora.objects.all()
        lista = []
        for bitacora in bitacoras:
            lista.append({
                'id': bitacora.id,
                'operacion': bitacora.operacion,
                'tabla': bitacora.tabla,
                'fecha': bitacora.fecha,
                'sintaxis_sql': bitacora.sintaxis_sql,
                'nombre_sql': bitacora.nombre_sql,
                'id_usuario': bitacora.id_usuario_id
            })
        return Response(lista)


class BitacoraIdView(APIView):
    @swagger_auto_schema(
        operation_description="Actualizar una bitácora por ID",
        request_body=BitacoraEntrada,
        responses={200: MensajeSalida})
    
    def put(self, request, id):
        bitacora = Bitacora.objects.get(id=id)
        bitacora.operacion = request.data.get('operacion')
        bitacora.tabla = request.data.get('tabla')
        bitacora.fecha = request.data.get('fecha')
        bitacora.sintaxis_sql = request.data.get('sintaxis_sql')
        bitacora.nombre_sql = request.data.get('nombre_sql')
        bitacora.id_usuario = request.data.get('id_usuario')
        bitacora.save()
        return Response({'mensaje': 'Bitácora actualizada exitosamente.'})


    @swagger_auto_schema(
        operation_description="Eliminar una bitácora por ID",
        responses={200: MensajeSalida}
    )
    
    def delete(self, request, id):
        bitacora = Bitacora.objects.get(id=id)
        bitacora.delete()
        return Response({'mensaje': 'Bitácora eliminada exitosamente.'})    