import cherrypy
import os
from lib.dbgestion import DbGestion
import requests

#Clase principal para que se vea que funciona.
class WebLSP(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        valorejem=self.insertardatos()
        valordat= self.datos("Un titulo", "2018", "0", "libro")
        return {"status":'OK', "rutas":{
            "insertardatos":{"nombre": "/insertardatos","json_ruta": valorejem},
            "datos":{"nombre":"/datos?titulo=Un+titulo&year=2018&mi_puntuacion=0&tipo=libro", "json_ruta": valordat}
            }}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def insertardatos(self, valor="No se pasa valor"):
        return {"status_ruta":'OK',"valor":valor}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def datos(self, titulo="", year=0, mi_puntuacion=0, tipo="" ):
        return {"status_ruta":'OK', "dato":{"titulo":titulo, "año": year, "puntuacion": mi_puntuacion, "tipo":tipo} }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def aa(self):
        return {"status_ruta":'OK',"valor":aa}
config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
    }
cherrypy.quickstart(WebLSP(),'/',config=config)
