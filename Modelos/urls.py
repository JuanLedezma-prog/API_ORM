from django.urls import path
from .views import FuncionarioView, FuncionarioIdView, UsuarioView, UsuarioIdView, IngresoView, IngresoIdView, BitacoraView, BitacoraIdView

urlpatterns = [
    path('funcionario/', FuncionarioView.as_view(), name='funcionario'),
    path('funcionario/<int:id>', FuncionarioIdView.as_view(), name='funcionario actualizar'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('usuario/<int:id>', UsuarioIdView.as_view(), name='usuario actualizar'),
    path('ingreso/', IngresoView.as_view(), name='ingreso'),
    path('ingreso/<int:id>', IngresoIdView.as_view(), name='ingreso actualizar'),
    path('bitacora/', BitacoraView.as_view(), name='bitacora'),
    path('bitacora/<int:id>', BitacoraIdView.as_view(), name='bitacora actualizar')
]