# Portfolio y blog personal

El portfolio y el blog se sirven desde Django. Las entradas se crean desde el panel de administración y aparecen ordenadas por fecha. Los comentarios se publican una vez aprobados por el administrador, que también puede eliminarlos.

## Ejecutar en Windows

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrí <http://127.0.0.1:8000/> para el portfolio, <http://127.0.0.1:8000/blog/> para el blog y <http://127.0.0.1:8000/admin/> para administrar entradas y comentarios. Al crear una entrada, completá título, slug, texto, fecha y, opcionalmente, un archivo multimedia.

La configuración incluida es para desarrollo local. Antes de publicar el sitio, configurá una clave secreta propia, `DEBUG=False`, hosts permitidos y almacenamiento/servidor para archivos multimedia.