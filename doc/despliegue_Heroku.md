# Despliegue en Heroku

### Pasos previos
- Clonar el repositorio que se quiere poner en Heroku.
      git clone https://github.com/GinesNC/LibSePeBOT-IV

- Tener las herramientas de Heroku instaladas en el sistema y loguearse. En mi caso me ha funcionado de esta forma:
      curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

### Siguientes pasos

- Ahora es el momento de crear la app. Desde el directorio donde se clonó el repositorio ejecutar:

      heroku apps:create --region eu <nombre>

    donde _nombre_ es un nombre cualquiera para la aplicación. Si no se indica se crea uno al azar que luego se pordrá modificar.

- Crear los ficheros: **runtime.txt** para especificar la versión de Python, **requirements.txt** para indicar las dependencias necesarias para que se ejecute la app y **Procfile** donde se dice que tiene que ejecutar la app.

- Hacer _git push heroku master_ para publicarlo.

- Por último ejecutar _heroku open_ para ver el resultado.

En mi caso he añadido el despliegue automático, en donde cuando hago push se pasa el test y se publica en Heroku. Esta opción se puede habilitar en la pestaña _Deploy_ de Heroku.
