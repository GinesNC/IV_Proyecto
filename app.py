import cherrypy
import os
class HelloWorld(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {"status":'OK'}

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 5000)),
    }
    }
cherrypy.quickstart(HelloWorld(),'/',config=config)
#cherrypy.config.update({'server.socket_host': '64.72.221.48',
#                        'server.socket_port': 80,
#                      })

# wsgi_app = cherrypy.Application(HelloWorld(), '/')
# if __name__ == '__main__':
# 	from wsgiref.simple_server import make_server
#
# 	httpd = make_server('', 6600, wsgi_app)
#     httpd.serve_forever()
