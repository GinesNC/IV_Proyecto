import cherrypy
import os
class WebLSP(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self,valor="No se pasa valor"):
        return {"status":'OK', "valor" : valor}



config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
    }
cherrypy.quickstart(WebLSP(),'/',config=config)
