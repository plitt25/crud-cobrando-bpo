
# **PRUEBA DE DESARROLLO COBRANDO BPO**


### Librerías :
- Django: [django](https://www.djangoproject.com/download/)

- # psycopg2: [psycopg2](https://pypi.org/project/psycopg2/)



## Instalación

Instalar con pip:

```
$ pip install -r requirements.txt
```

## Estructura 
```
.
|────COBRANDO_BPO
|──────_init_.py
|──────asgi.py
|──────settings.py
|──────urls.py
|──────wsgi.py

|────manage.py
|────.gitignore.py


APPS

|────EMPLEADOS
|──────migrations/
|──────templates/
| |────editEmpleados.html
| |────list_empleados.html
|────admin.py
|────apps.py
|────models.py
|────tests.py
|────urls.py
|────view.py



```


## REQUISITOS


Teniendo en cuenta el siguiente modelo elabore un micro servicio para la tabla “empleado” el cual sea capaz de insertar, actualizar, borrar y consultar (CRUD) información utilizando el FrameWork de Django:


![image](https://images2.imgbox.com/52/c1/fAg0hBGa_o.png)


El micro servicio tiene que interactuar con una DB de tipo POSTGRESQL, además de esto, es un plus si realiza el montaje por medio de Docker, aunque no es completamente necesario, su micro servicio tiene que estar disponible por el puerto 1234 además de tener las indicaciones pertinentes de uso.       

