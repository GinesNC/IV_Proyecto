import cherrypy
import os
from lib.libsepe import libsepe
#Clase principal para que se vea que funciona.
class WebLSP(object):

    @cherrypy.expose
    def index(self,valor="No se pasa valor"):
        return """<html>
          <head></head>
          <body>
            Página principal <br><br>
            <a href='insertardatos'> Insertar Datos </a> <br><br>
            <a href='status'> Status </a><br><br>
            Valor = """ + valor +"""
          </body>
        </html>"""

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def status(self):
        status={"status":'OK'}
        return status

    @cherrypy.expose
    def insertardatos(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="datos">
              Titulo: <input type="text" name="titulo" />
              Año: <input type="text" name="year" />
              Puntuacion: <input type="text" name="mi_puntuacion" />
              Tipo: <input type="text" name="tipo" />
              <button type="submit">Enviar</button>
            </form>
          </body>
        </html>"""

    global dat
    dat=""
    @cherrypy.expose
    def datos(self, titulo="", year=0, mi_puntuacion=0, tipo="" ):
        global dat
        dat=libsepe.crear_dato(titulo,year,mi_puntuacion,tipo)
        return "los datos introducidos han sido\n Titulo: " + titulo + "\n año: "+year + "\nPuntuacion: "+ mi_puntuacion + "\ntipo: " + tipo + """<br> el json creado aqui: <a href='/json'> json</a> """


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def json(self):
        return dat

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
    }
cherrypy.quickstart(WebLSP(),'/',config=config)
