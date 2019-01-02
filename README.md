[![Build Status](https://travis-ci.org/GinesNC/LibSePeBOT-IV.svg?branch=master)](https://travis-ci.org/GinesNC/LibSePeBOT-IV)


# LibSePeBOT
## Introducción

La idea de este proyecto es un servicio web en el que poder llevar un control de las series y películas que se han visto así como las que se quieren ver y de los libros que se han leído y se quieren leer. Dicha información podrá ser tanto datos almacenados del usuario como de páginas de opiniones, por ejemplo de [IMDb](https://www.imdb.com/).

En los siguientes apartados se detalla su estructura y las herramientas usadas.

## Estructura

La parte visual o front-end, es una página web simple donde se podrá interactuar mediante el envío de mensajes o de comandos, por formulario o URL. La parte oculta, back-end, es un microservicio donde se interpreten los mensajes recibidos por el usuario y se envíe una respuesta acorde a ese mensaje o comando. En esta parte se gestiona todo lo relacionado con las bases de datos, así como en el caso de solicitarlo, proporcionar calificaciones y opiniones de diferentes páginas relacionadas.

## Heramientas

- El lenguaje de esta aplicación es Python.
- El framework [CherryPy](https://cherrypy.org/)
- Como base de datos [MongoDB](https://www.mongodb.com/es).
- Para los test el módulo __unittest__
- Para la integración continua [Travis CI](https://travis-ci.org/).
- Como PaaS [Heroku](https://www.heroku.com/)


He elegido CherryPy como framework porque que es estable, está creciendo, tiene 10 años y actualmente tiene mucha actividad. Al ser orientado objetos, permite hacer un código más limpio y un desarrollo más rápido. A parte tiene buen rendimiento y permite trabajar en la versión 2 y 3 de Python.

La base de datos que he elegido es NoSQL, y en este caso MongoDB porque solo se va a almacenar datos de forma plana y variables del estilo:

      Por ejemplo una película tendrá los campos (aproximados):
        titulo: "titulo", año: "XXXX", mi_puntuacion: [0..10], usuario: <uid del bot> ...

Por lo que de este modo me ahorro espacio en disco.
___________________________________

## Integración continua y test

La clase que se testea es a la que yo he llamado [_DbGestion_](https://github.com/GinesNC/LibSePeBOT-IV/blob/master/lib/DbGestion.py). Actualmente hay unas funciones básicas. El encargado de testear dichas funciones es la clase [_Test_](https://github.com/GinesNC/LibSePeBOT-IV/blob/master/test.py). Algunas funciones son que se inserta correctamente un dato, se modifica o se borra.

Para que Travis CI funcione hay que añadir el correspondiente [.travis.yml](https://github.com/GinesNC/LibSePeBOT-IV/blob/master/.travis.yml). La estructura de este fichero es como lo que sigue:

      language: python
      python:
        - "3.6"
      install:
        - pip3 install -r requirements.txt
      script:
        - python3 test.py


 en el cual se especifica el lenguaje y versión del proyecto, las dependencias necesarias para que funcione y como se ejecuta el test. Tras cada _git push_, Travis se pone en funcionamiento y lo testea. El resultado del test se puede ver en [![Build Status](https://travis-ci.org/GinesNC/LibSePeBOT-IV.svg?branch=master)](https://travis-ci.org/GinesNC/LibSePeBOT-IV).

___________________________________

## Despliegue PaaS
En este momento se puede ver que la aplicación funciona en Heroku y muestra un json con un estado, junto con las rutas y los parámetros que se le pueden pasar.

Despliegue: https://libsepebot.herokuapp.com [![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://libsepebot.herokuapp.com)

El como desplegar con Heroku se puede ver en la [documentación](doc/despliegue_Heroku.md).

___________________________________

## Docker y Heroku

La aplicación se encuentra en [DockerHub](https://hub.docker.com/r/ginesnc/libsepebot-iv/).

El contenedor [desplegado en Heroku](https://libsepebot-docker.herokuapp.com) [![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://libsepebot-docker.herokuapp.com)

[En este archivo](doc/Docker.md) se explica como se hace el despliegue automático, así como la publicación del contenedor en Heroku.


___________________________________

## Despliegue en Azure desde 0

Despliegue: 40.112.90.212

En el puerto 8443

El como se ha llevado a cabo esta tarea se puede leer [aquí](doc/despliegue_azure_de0.md)
