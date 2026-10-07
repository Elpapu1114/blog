Este proyecto es un portfolio y blog personal desarrollado con Django. Permite mostrar información del portfolio y publicar diferentes entradas desde un panel de administracion

El blog lo que hace es mostrar publicaciones con titulo, descripcion, fecha de publicacion y fotos.
Este cuenta con un sistema de comentarios. En el cual los usuarios pueden dejar y el admnistrador si no le gusta lo puede borrar

Funciones principales

Portfolio personal
Publicacion de entradas
Titulo, texto, fecha y contenido multimedia en cada publicacion
Publicaciones ordenadas por fecha
Sistema de comentarios
Aprobacion de comentarios desde el administrador
Eliminacion de comentarios
Panel de administracion de Django

## Ejecutar en Windows

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrí <http://127.0.0.1:8000/> para el portfolio, <http://127.0.0.1:8000/blog/> para el blog y <http://127.0.0.1:8000/admin/> para administrar entradas y comentarios. Al crear una entrada, completá título, slug, texto, fecha y, opcionalmente, un archivo multimedia.

La configuración incluida es para desarrollo local. Antes de publicar el sitio, configurá una clave secreta propia, `DEBUG=False`, hosts permitidos y almacenamiento/servidor para archivos multimedia.

