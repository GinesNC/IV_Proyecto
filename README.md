[![Build Status](https://travis-ci.org/GinesNC/LibSePeBOT-IV.svg?branch=master)](https://travis-ci.org/GinesNC/LibSePeBOT-IV)

[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://libsepebot.herokuapp.com)
# LibSePeBOT
## Introducción

La idea de este proyecto es realizar un servicio web en el que poder llevar un control de las series y películas que se han visto así como las que se quieren ver y de los libros que se han leído y se quieren leer.  ~~Para llevar a cabo esto, realizaré un bot en Telegram donde se pueda visualizar e interactuar para el cambio de información~~. Dicha información podrá ser tanto datos almacenados del usuario como de páginas de opiniones, por ejemplo de [IMDb](https://www.imdb.com/).

En los siguientes apartados se detalla su estructura y las herramientas que se utilizarán para el desarrollo.

## Estructura

La parte visual o front-end, será ~~un bot de Telegram~~ una página web simple donde se podrá interactuar mediante el envío de mensajes o de comandos, por formulario o URL. La parte oculta, back-end, será un microservicio donde se interpreten los mensajes recibidos por el usuario y se envíe una respuesta acorde a ese mensaje o comando. En esta parte se gestionará todo lo relacionado con las bases de datos, así como en el caso de solicitarlo, proporcionar calificaciones y opiniones de diferentes páginas relacionadas.

## Heramientas

- El lenguaje para desarrollar esta aplicación será Python.
- El framework [CherryPy](https://cherrypy.org/)
- ~~La API [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).~~
- Como base de datos usaré una NoSQL y será [MongoDB](https://www.mongodb.com/es).
- Para pruebas en local usaré una máquina virtual.
- Para los test usaré el módulo __unittest__
- Para la integración continua usaré [Travis CI](https://travis-ci.org/).
- Como PaaS he usado [Heroku](https://www.heroku.com/)

He elegido CherryPy como framework porque que es estable, está creciendo, tiene 10 años y actualmente tiene mucha actividad. Al ser orientado objetos, permite hacer un código más limpio y un desarrollo más rápido. A parte tiene buen rendimiento y permite trabajar en la versión 2 y 3 de Python.

La base de datos que he elegido es NoSQL, y en este caso MongoDB porque solo se va a almacenar datos de forma plana y variables del estilo:

      Por ejemplo una película tendrá los campos (aproximados):
        titulo: "titulo", año: "XXXX", mi_puntuacion: [0..10], usuario: <uid del bot> ...

Por lo que de este modo me ahorro espacio en disco.
___________________________________

## Integración continua y test

En este caso la clase que se va a testear es a la que yo he llamado [_libsepe_](https://github.com/GinesNC/LibSePeBOT-IV/blob/master/lib/libsepe.py). Actualmente hay unas funciones de prueba, pero en el futuro irán las funciones principales. El encargado de testear dichas funciones es la clase [_Test_](https://github.com/GinesNC/LibSePeBOT-IV/blob/master/test.py). Algunas funciones son que se inserta correctamente un dato, se modifica o se borra. Estos test avanzarán a lo largo del proyecto.

Para la integración continua he usado Travis CI junto con el correspondiente [.travis.yml](https://github.com/GinesNC/LibSePeBOT-IV/blob/master/.travis.yml) en el cual se especifica el lenguaje y versión del proyecto, las dependencias necesarias para que funcione y como se ejecuta el test. Tras cada git push, Travis se pone en funcionamiento y lo testea. El resultado se puede ver, en mi caso, en la etiqueta que hay al principio.

___________________________________

## Despliegue PaaS
[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://libsepebot.herokuapp.com)
En este momento se puede ver que la aplicación funciona en Heroku y muestra un json con información de que funciona y un valor. El valor se puede cambiar como en el ejemplo *"/?valor=Nuevo+valor"*

El como desplegar en Heroku se puede ver en la [documentación](doc/despliegue_Heroku.md).
