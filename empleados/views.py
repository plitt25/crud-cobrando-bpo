from django.shortcuts import render, redirect
from .models import Departamento, Empleado

# Create your views here.
def list_empleados(request):
    empleado = Empleado.objects.all()
    return render(request, 'list_empleados.html', {"empleados": empleado})

def delete_empleados(request, empleado_id):
    empleado=Empleado.objects.get(id=empleado_id)
    empleado.delete()
    return redirect('/empleados/')

def edit_empleados(request):
    r = Departamento(codigo=request.POST['codigo'], nombre='quemado', presupuesto='quemado')
    r.save()
    empleado =Empleado(codigo=request.POST['codigo'],nif=request.POST['nif'], nombre=request.POST['nombre'], apellido1=request.POST['apellido1'], apellido2=request.POST['apellido2'],codigo_departamento=request.POST['codigo_departamento'], departamento=r)
    empleado.save()
    return redirect('/empleados/')

def edicion_empleados(request, empleado_id):
    empleado=Empleado.objects.get(id=empleado_id)
    return render(request, "editEmpleados.html", {"empleados": empleado})

def create_empleados(request):
    r = Departamento(codigo=request.POST['codigo'], nombre='Smith', presupuesto='152')
    r.save()
    empleado =Empleado(codigo=request.POST['codigo'],nif=request.POST['nif'], nombre=request.POST['nombre'], apellido1=request.POST['apellido1'], apellido2=request.POST['apellido2'],codigo_departamento=request.POST['codigo_departamento'], departamento=r)
    empleado.save()
    return redirect('/empleados/')

