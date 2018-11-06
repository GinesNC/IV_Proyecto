import cherrypy
import os
#Clase principal para que se vea que funciona.
class WebLSP(object):

    @cherrypy.expose
    def index(self):
        return """
        <a href='/status'> Estado </a>
         """, {"status":'OK'}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def status(self,valor="No se pasa valor"):
        return {"status":'OK', "valor" : valor}

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
    }
cherrypy.quickstart(WebLSP(),'/',config=config)
