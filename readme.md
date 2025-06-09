# Tabla de contenido

## Introduccion.

- Introducción.
- Finalidad.
- Objetivos.
- Medios necesarios.
- Planificación.

## Realización del Proyecto.

- Trabajos realizados.
- Problemas encontrado.
- Modificaciones sobre el proyecto planteado inicialmente
- Posibles mejoras al proyecto
- Bibliografía.

## Introducción.

### Introducción.

Crear una aplicación web que muestre los juegos nuevos que salgan, las noticias de cada uno de ellos
si disponen de tales, mostrar o buscar juegos con su número de trofeos, marcar aquellos juegos que sean gratuitos o de pago,
mostrar los juegos jugados recientemente por el usuario y que pueda todos sus juegos, además, podrá ver que trofeos tiene
desbloqueado y cuales les falta por desbloquear.

Servir una api, que permita obtener diferentes datos para futuros desarrolladores y la cual va a permitir que nuestra aplicación web
pueda obtener todos estos datos

### Finalidad.

Tener a disposición de forma muy accesible y sencilla el poder ver los trofeos que te quedan
por sacar de un juego, aquellos trofeos que tienes, juegos a los que has jugado reciéntemente, buscar juegos y ver si son de pago o no.

### Objetivos.

Vamos a poder tanto iniciar sesión como registrarnos, actualizar nuestro perfil, vamos a poder buscar u observar los juegos que hay, los trofeos que tienen
ver si son gratis o no, ver las ultimas noticas de los juegos (actualizacions, corrección de errores...),
ver todas las noticas con su correspondiente botón de ir a la fuente de la noticia, poder ver nuestros juegos jugados reciéntemente,
poder saber que trofeos hemos logrado obtener de cada uno de nuestros juegos.

Tambien damos la posibilidad de que futuros desarrolladores que tengan una idea similiar a la nuestra, puedan acceder a nuestra api,
para que puedan programar su propia aplicación sin tener que pasar por docuemntaciones poco familiares y robustas.

### Medios necesarios.

- Un PC de configuración media/alta para manejar localmente servidores y desarrollar.
- VScode o Pycharm para desarrollar.
- Docker, Docker-compose
- Cuenta en aws con privilegios suficientes.
- Máquina en aws EC2 donde irá todo el backend de la aplicación (django, redis, celery, celery beat, postgreSQL)
- Bucket en aws S3 donde irá nuetro frontend
- Git para poder desarrollar funcionalidades entre ramas y combinarlas, entre muchas más funcionalidades.
- Cuenta de Github.
- Actions de Github que hagan el despliegue automáticamente.

### Planificación.

## Realización del Proyecto.

### Problemas encontrados

- Problemas al serializar las fechas ya que steam devuelve fechas en distintos formatos.
- Obtener el contador de los trofeos mediante el serializador.
- Impelementación de steam.
- Crear los juegos.
- Crear los trofeos.
- Obtener los juegos de un usuario e identificar cuales tiene y cuales no.
- Problemas con el slider de react.

### Trabajos realizados

- Creación de la app trophy_hunters de django.
- Creación de los endpoints de nuestra api.
- Creacion de sus vistas.
- Creación de los modelos que se va a usar.
- Creacion de los serializares que crean datos y de aquellos que los muestran.
- Añadir los ajustes necesarios a nuestro backend.
- Añadir filtros para poder filtrar nuestra información de la base de datos y sea mucho más accesible.
- Añadir drf-spectacular para que se genere una documentación automática en endpoint que permite visualizar todos nuestros endpoints.
- Añadir JWT en django para autenticar a los usuarios del front.
- Cambiar la base de datos a postgreSQL.
- Implementar celery + celery beat para las task programadas.
- Creación de las task programadas.
- Creación del horario de las tareas.
- Crear requirements.txt para poder instalar las dependencias de nuestro backend de forma automática con docker.
- Dockerizar el proyecto.
- Creación del frontend con react + vite.
- Uso de tailwindcss para darle estilos a nuestra app de react.
- Uso de MUI para meter componentes como mensajes.
- Creación de los componentes necesarios de react.
- Creación del contexto user para pasar información entre componentes para saber si esta logged, su perfil, etc.
- Meter imágenes para su uso.
- Crear los actions de github que permitirán el despliegue automatico de nuestra app (frontend + backend)
- Crear máquina EC2 en aws para meter nuestro backend.
- Implementar las políticas de seguridad de la máquina para permitir el tráfico saliente y entrante.
- Crear un bucket en una S3 para poder meter nuestro frontend.

### Modificaciones sobre el proyecto planteado inicialmente

- Iniciar sesión con Steam
- Usar Kubernetes
- Implementar IA

### Posibles mejores al proyecto.

- Añadir estadísticas de cuenta, juegos y trofeos.
- Donaciones.
- Crear guías de juegos.
- Iniciar sesion con multiples plataformas (google, facebook...)
- Mejoras de estilos e interfaz de usuario.

### Bibliografía.

- [Stackoverflow](https://stackoverflow.com/questions)
- [Django docs](https://docs.djangoproject.com/en/5.2/)
- [Drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/readme.html#installation)
- [drf-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
- [drf](https://www.django-rest-framework.org/)
- [Django-filters](https://django-filter.readthedocs.io/en/stable/guide/usage.html)
- [Curso React](https://openwebinars.net/academia/aprende/react/24794/)
- [React doc](https://react.dev/)
- [Steam doc](https://developer.valvesoftware.com/wiki/Steam_Web_API#GetNewsForApp_.28v0001.29)
- [Steam doc 2](https://wiki.teamfortress.com/wiki/WebAPI#General_interfaces)