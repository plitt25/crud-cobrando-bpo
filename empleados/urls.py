from django.urls import path
from .views import list_empleados, create_empleados, delete_empleados, edicion_empleados, edit_empleados

urlpatterns = [
    path('',list_empleados),
    path('new/', create_empleados, name='create_empleados'),
    path('delete_empleados/<int:empleado_id>/', delete_empleados, name='delete_empleados'),
    path('edicion_empleados/<int:empleado_id>/', edicion_empleados, name='edicion_empleados'),
    path('edit_empleados/', edit_empleados, name='edit_empleados')
]
