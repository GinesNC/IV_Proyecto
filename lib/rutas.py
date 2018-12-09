import json


def status():
    return json.dumps({'status':'OK'})


def insertardatos(valor="No se pasa valor"):
    return json.dumps({"status":'OK',"valor":valor})


def datos(titulo="", year=0, mi_puntuacion=0, tipo="" ):
    return json.dumps({"status":'OK', "dato":{"titulo":titulo, "año": year, "puntuacion": mi_puntuacion, "tipo":tipo} })


def index(valor="No se pasa valor", titulo="", year=0, mi_puntuacion=0, tipo="" ):
    valorejem=json.loads(insertardatos(valor))
    valordat= json.loads(datos(titulo, year, mi_puntuacion, tipo ))
    return json.dumps({"status":'OK', "rutas":{
        "insertardatos":{"nombre": "/insertardatos","json_ruta": valorejem},
        "datos":{"nombre":"/datos?titulo=Un+titulo&year=2018&mi_puntuacion=0&tipo=libro", "json_ruta": valordat},
        "status": {"nombre": "/status","status":"OK"}
        }
        })
