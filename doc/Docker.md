# Despliegue en Docker

### Despliegue automático
Para poder hacer el despliegue automático en Docker Hub cuando se hace un push hay que crear un repositorio que lo permita. Para eso se hacer clic en _Create_ y en el menú desplegable se elige la segunda opción: _Create Automated Build_.

![img](capturas/automated-build.png)

El siguiente paso es elegir desde donde se quiere hacer el despliegue automático, GitHub o Bitbucker. En mi caso con GitHub, que ya tenía asociada la cuenta. Ahora es el momento de elegir el repositorio del cual se hace el despliegue automático y por último se configura el repositorio de Docker Hub, escribiendo una descripción del mismo, poniendo que visibilidad tendrá (publica o privada). Si el Dockerfile se encuentra en otra rama que no es la master u otra localización hay que indicarlo.

![cab](capturas/cab.png)

El Dockerfile es un fichero en el cual se indica como se crea el contenedor y que debe ejecutar.

    FROM python:3

    WORKDIR /usr/src/app

    COPY . .
    RUN pip install --no-cache-dir -r requirements.txt

    CMD [ "python", "./app.py" ]



En este caso se crea un contenedor con la imagen python oficial. He elegido esta porque se hace mas rápido el despliegue, puesto que no se tiene que poner en marcha un sistema operativo e instalar posteriormente el lenguaje y las dependencias necesarias.

Para que no se copien archivos innecesarios hay que crear el fichero _.dockerignore_ e indicarle aquellos archivos que no se tienen que copiar en el contenedor como los test o el archivo de la licencia . En mi caso:

    *.yml
    test.py
    LICENSE
    Procfile

<!--* -->


### Despliegue contenedor en Heroku

Para este caso hay que crear un nuevo fichero, _heroku.yml_


    build:
      docker:
        web: Dockerfile

En este fichero se pueden poner varias secciones. En mi caso he puesto en _build_ que se instale docker y donde se encuentra el Dockerfile que genera la imagen. Si no se pone la sección _run_ se usa el CMD del Dockerfile.

Después de crear los ficheros hay que poner la pila de la aplicación en el contenedor: `heroku stack:set container` y hacer push de la aplicación a Heroku. Una vez hecho esto usará el heroku.yml y no el Procfile.
