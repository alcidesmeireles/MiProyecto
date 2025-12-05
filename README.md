# MiProyecto
MiProyecto — Sistema de Gestión de Repuestos de Autos

Entrega Final – Curso de Python

Este proyecto es una aplicación web desarrollada con Django que permite administrar repuestos de autos, gestionar usuarios con perfiles personalizados e incluir funcionalidades completas de CRUD, autenticación y navegación mediante templates con herencia.

 -- Contenido del Proyecto

El sistema incluye:

- Navegación y estructura
- NavBar con acceso a:
- Home
- About
- Login / Signup
- Perfil de usuario
- CRUD de Repuestos (si estás logueado)
- Plantilla base con herencia de templates.

-- Aplicaciones incluidas

inventario: CRUD del modelo principal Repuesto + modelos auxiliares

accounts: manejo de usuarios, registro, login, logout, edición de perfil y avatar

Modelo principal: Repuesto

Cumple los requisitos mínimos:
2 campos CharField: nombre, descripcion
1 campo ImageField: imagen
1 campo DateField: fecha_ingreso
1 campo IntegerField con unique=True: codigo
Asociado a una marca (ForeignKey)

-- Funcionalidades CRUD (Repuestos)

Listado (con buscador y mensaje si no hay resultados)

Detalle de cada repuesto

Crear (solo usuarios logueados)

Editar (solo usuarios logueados)

Eliminar (solo usuarios logueados)

Implementado con Class Based Views (CBV):

ListView

DetailView

CreateView

UpdateView

DeleteView

Incluye uso de:

LoginRequiredMixin (requisito)

Un decorador @login_required en una view funcional (requisito)

-- Sistema de usuarios (accounts)

Signup (username, email, password)

Login / Logout

Perfil visible para cada usuario

Edición del perfil:

Avatar

Biografía

Link

Fecha de nacimiento

Cambio de contraseña

Todos los perfiles se crean automáticamente mediante señales (signals)

-- Vistas adicionales

Home

About (about/)

-- Administración (Django Admin)

Todos los modelos están registrados:

Marca

Repuesto

Cliente

Profile

-- Instalación y configuración

1) Clonar el repositorio
git clone https://github.com/alcidesmeireles/MiProyecto.git
cd miproyecto

2) Crear y activar entorno virtual (recomendado)
En Windows
python -m venv venv
venv\Scripts\activate

3) Instalar dependencias
pip install -r requirements.txt

Importante: el proyecto usa Pillow para manejar imágenes.

4) Realizar migraciones
python manage.py makemigrations
python manage.py migrate

5) Crear un superusuario (opcional)
python manage.py createsuperuser

6)  Ejecutar el servidor
python manage.py runserver

Ahora abrí en tu navegador:
 http://127.0.0.1:8000/