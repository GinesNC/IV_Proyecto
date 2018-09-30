# LibSePeBOT
## Introducción

La idea de este proyecto es realizar un servicio web en el que poder llevar un control de las series y películas que se han visto así como las que se quieren ver y de los libros que se han leído y se quieren leer. Para llevar a cabo esto, realizaré un bot en Telegram donde se pueda visualizar e interactuar para el cambio de información. Dicha información podrá ser tanto datos almacenados del usuario como de paginas de opiniones, por ejemplo de [IMDb](https://www.imdb.com/).

En los siguientes apartados se detalla su estructura y las herramientas que se utilizaran para el desarrollo.

## Estructura

La parte visual o front-end, será un bot de Telegram en el cual se podrá interactuar mediante el envío de mensajes o de comandos. La parte oculta, back-end, será un microservicio donde se interpreten los mensajes recibidos por el usuario y se envíe una respuesta acorde a ese mensaje o comando. En esta parte se gestionará todo lo relacionado con las bases de datos, así como en el caso de solicitarlo, proporcionar calificaciones y opiniones de diferentes páginas relacionadas.

## Heramientas

- El lenguaje para desarrollar esta aplicación será Python.
- El framework [CherryPy](https://cherrypy.org/)
- La API [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).
- Como base de datos usaré una NoSQL y será MongoDB.

Las razones que me han llevado a elegir Python es que es un lenguaje que estoy aprendiendo y me siento más cómodo, al igual que la API. Con respecto al framework, CherryPy ha sido mi elección. Es un framework que es estable, está creciendo, tiene 10 años y actualmente tiene mucha actividad. Al ser orientado objetos, permite hacer un código más limpio y un desarrollo mas rápido. A parte tiene buen rendimiento y permite trabajar en la versión 2 y 3 de Python.

La base de datos que he elegido es una NoSQL, y en este caso MongoDB, ya que al igual que la API y el lenguaje de programación es un sistema que ya he usado, por lo que me resulta más familiar. Aparte de esto he decidido poner los datos en una base de datos no relacional porque solo se va a almacenar información plana y variables del estilo:

      Por ejemplo una película tendrá los campos (aproximados):
        titulo: "titulo", año: "XXXX", mi_puntuacion: [0..10], usuario: <uid del bot> ...

Por lo que de este modo me ahorro espacio en disco.
