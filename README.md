## Proyecto Coder Python Paola Arena - Fabiana Torres Meza
### Pasos a seguir para desplegar el proyecto
1. Clonar repositorio
    `git clone https://github.com/FabianaTM/Entrega1-Arena-TorresMeza.git`
2. Crear entorno virtual
    `python -m venv venv`
3. Activar entorno virtual
    `. start.sh`
4. Instalar paquetes necesarios en archivo requirement.txt
    `pip install -r requirement.txt`
5. Generar tablas de la base de datos
    `python manage.py migrate`
6. Levantar servicio
    `python manage.py runserver`
7. Navegar por distintas pestañas
    `http://127.0.0.1:8000`
8. Registrar usuario
    `http://127.0.0.1:8000/accounts/registrar/`
9. Iniciar sesión con usuario creado
    `http://127.0.0.1:8000/accounts/login/`
10. Crear mascota desde pestaña Crear
    `http://127.0.0.1:8000/crear_mascota`
11. Buscar mascotas desde pestaña Ver
    `http://127.0.0.1:8000/ver_mascota`
12. Ver información de perfil y editar datos
    `http://127.0.0.1:8000/accounts/perfil/`
13. Navegar por distintas secciones de la página

