## Proyecto Coder Python
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
8. Crear personas desde pestaña Crear
    `http://127.0.0.1:8000/crear_persona`
9. Buscar personas desde pestaña Ver
    `http://127.0.0.1:8000/ver_persona`