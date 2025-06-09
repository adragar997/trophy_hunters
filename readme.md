# Documentación TrophyHunters

## Esta es una aplicación creada y diseñada por Alexander Drapala García.

Con esta app, podemos obtener los juegos de steam, sus trofeos asociados, los juegos de un usuario, los trofeos que ha ido consiguiendo y si lo tiene o no desbloqueados, además de poder ver las noticias de cada juego.

## Índice

- [Configuración del área de trabajo](#configuración-del-área-de-trabajo)
    - [Clonar el repositorio ](#clonar-el-repositorio)
    - [Crear entorno virtual y activarlo](#crear-entorno-virtual-oculto-y-activarlo)
    - [Instalar requirements.txt](#instalar-requirementstxt)
    - [Instalar dependecias del frontend](#instalar-dependecias-del-frontend)
    - [Instalar docker y docker-compose](#instalar-docker-y-docker-compose)
        - [Windows](#windows)
        - [Linux](#linux)
    - [Arrancar el backend](#arrancar-el-backend)
- [Empezar a desarrollar](#empezar-a-desarrollar)
    - [Estructura de TrophyHunters](#estructura-de-trophyhunters)
- [Despliegue](#despliegue)
    - [EC2](#ec2)
    - [S3](#s3)

## Configuración del área de trabajo

### Clonar el repositorio:

`git clone urlHtpp`
 
### Crear entorno virtual oculto y activarlo

Entrar en la carpeta trophy_hunters (si hay mas seguimos entrando) hasta que veamos las carpetas *backend* y *frontend*

`python -m venv .venv` 

`source .venv/bin/activate`

### Instalar requirements.txt

Dentro de la carpeta de backend esta el archivo requirements.txt para instalar todas las dependecias que usaremos.

`pip install -r requirements.txt`

### Instalar dependecias del frontend

Dentro de la carpeta frontend ejecutamos el siguiente comando:

`npm install`

### Instalar docker y docker-compose

#### Windows

Para instalar docker en windows instalamos el launcher de [*Docker desktop*](https://www.docker.com/products/docker-desktop/)

#### Linux

```
sudo apt update
sudo apt upgrade

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### Arrancar el backend

SI USAS UN .ENV LUEGO TIENES QUE AÑADIR ESAS VARIABLES AL COMPOSE

Para que nuestro backend comience a funcionar, necesitamos levantar el contenedor (dentro de la carpeta backend donde esta el docker-compose.yml) ejecutando el siguiente comando:

- -d levanta el contenedor en modo demon (background) 
- --build forzamos a que vuelva hacer una imagen del la app con los cambios que aplicamos (si hemos desarrollado algo)

`docker compose up -d --build`

### Arrancar el frontend

Para que nuestro fronend comience a funcionar, necesitamos arrancar el servidor (dentro de la carpeta frontend) ejecutando el siguiente comando:

`npm run dev`

## Empezar a desarrollar

### Estructura de TrophyHunters

```
trophy_hunters
├───.github
│   └───workflows
│           sync-frontend-backend.yml
│          
├───backend
│   ├───config
│   │   │   asgi.py
│   │   │   celery.py
│   │   │   settings.py
│   │   │   urls.py
│   │   │   wsgi.py
│   │   │   __init__.py
│   │   │   
│   │   └───__pycache__
│   ├───letsencrypt 
│   ├───media
│   │   ├───profile_banners
│   │   │       
│   │   └───profile_pictures
│   └───trophy_hunters
│       │   admin.py
│       │   apps.py
│       │   fetch_data.py
│       │   filters.py
│       │   models.py
│       │   serializers.py
│       │   tasks.py
│       │   tests.py
│       │   urls.py
│       │   views.py
│       │   __init__.py
│       ├───migrations
│       │   │   __init__.py
│       │   │   
│       │   └───__pycache__
│       │           __init__.cpython-313.pyc
│       │           
│       └───__pycache__
│               admin.cpython-313.pyc
│               apps.cpython-313.pyc
│               fetch_data.cpython-313.pyc
│               filters.cpython-313.pyc
│               models.cpython-313.pyc
│               serializers.cpython-313.pyc
│               tasks.cpython-313.pyc
│               urls.cpython-313.pyc
│               views.cpython-313.pyc
│               __init__.cpython-313.pyc
│               
└───frontend
    │   .gitignore
    │   eslint.config.js
    │   index.html
    │   package-lock.json
    │   package.json
    │   postcss.config.js
    │   tailwind.config.js
    │   vite.config.js
    └───src
        │   
        ├───assets
        │   └───static
        │           
        └───components
            │   
            └───Context
                    

```

## Despliegue

Al hacer un push a dev, se activan los **Github actions** que replican el contenido de las carpetas **backend** y **frontend**, estas se suben a la rama remota de cada una de ellas e inmediátamente después, se despliegan a sus máquinas correspondientes en **AWS**.

### EC2

Máquina ubuntu que acepta peticiones 0.0.0.0/0 y tiene los puertos activados 443 HTTPS, 80 HTTP, 8080, 22 SSH.

### S3


Un bucket que permite las conexiones externas y la cual se sube la carpeta dist/ al hacer `npm run build`. Todo esta automatizado por el **action**.






