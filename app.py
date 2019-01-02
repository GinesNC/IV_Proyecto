import cherrypy
import os
from lib.dbgestion import DbGestion
import lib.rutas as rutas
import requests

import json

class WebLSP(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return json.loads(rutas.index("No se pasa valor", "Un titulo", "2018", "0", "libro"))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def insertardatos(self, valor="No se pasa valor"):
        return json.loads(rutas.insertardatos(valor))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def datos(self, titulo="", year=0, mi_puntuacion=0, tipo="" ):
        return json.loads(rutas.datos(titulo, year, mi_puntuacion, tipo))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def status(self):
        return json.loads(rutas.status())


config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 80)),
    }
    }
cherrypy.quickstart(WebLSP(),'/',config=config)
