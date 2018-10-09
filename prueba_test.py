import unittest
import pymongo
import random


def conectarColeccion(pruebas):
    """Con esto se establece la conexion con MongoDB y devuelve la coleccion
    correspondiente si es test o no.

    Devuelve la coleccion libsepe_dat si no es una prueba, en caso contrario la
    coleccion para hacer test.

    Parámetros:
    pruebas -- Puede ser True o False. Se utiliza para elegir la coleccion.

    """
    try:
        conn=pymongo.MongoClient('localhost', 27017)
        print("Conexion OK!!!")
    except(pymongo.errors.ConnectionFailure, e):
        print("No se puede conectar MongoDB: %s") % e

    db = conn['lsp_db']
    if pruebas:
        return db['test_pruebas']
    else :
        return db['libsepe_dat']

def insertarDatos(coleccion, datos):
    """Funcion para insertar datos en la colleccion donde va almacenado todo.

    Devuelve True si se ha insertado correctamente y se crea una instancia de
    InsertOneResult, en caso contrario False.

    Parámetros:
    coleccion -- es la coleccion que donde se hace la inserccion
    datos -- es un diccionario que se utilizará para insertar los datos en la
        colleccion. Tiene una estructura donde va el tipo de contenido que es
        (pelicula, libro o serie), el titulo, el año, una puntuacion propia y
        el usuario del que es dicho dato. Esto se alamcena en la base de datos:
        - lsp_db y en la colleccion libsepe_dat.

    """
    x = coleccion.insert_one(datos)

    return isinstance(x, pymongo.results.InsertOneResult)


def modificarDatos(coleccion, titulo, new_datos, uid):
    """Funcion para modificar datos de la colleccion donde va almacenado todo.

    Devuelve True si se ha modificado correctamente y se crea una instancia de
    UpdateResult, en caso contrario False.

    Parámetros:
    coleccion -- es la coleccion que donde se hace la modificacion
    titulo -- Es el titulo exacto, igual que esta en la colleccion, del dato que
        se quiere modifcar. Se puede modificar el titulo también si así se quisiera.
    new_datos -- es un diccionario donde estan los nuevos datos.
    uid -- Es el indicador del usuario, para poder modificar un valor debe
        coincidir el titulo y el uid. Este valor es el unico que no se puede modificar.

    """
    query = {'titulo' : titulo, 'uid' : uid}
    x = coleccion.update_one(query, {'$set' :new_datos})

    return isinstance(x, pymongo.results.UpdateResult)

def eliminarDatos(coleccion, titulo, uid):
    """Funcion para eliminar datos de la colleccion donde va almacenado todo.

    Devuelve True si se ha eliminado correctamente y se crea una instancia de
    DeleteResult, en caso contrario False.

    Parámetros:
    coleccion -- es la coleccion que donde se hace la eliminacion
    titulo -- Es el titulo exacto, igual que esta en la colleccion, del dato que
        se quiere eliminar.
    uid -- Es el indicador del usuario, para poder eliminar un valor debe
        coincidir el titulo y el uid.


    """
    query = {'titulo' : titulo, 'uid' : uid}
    x = coleccion.delete_one(query)

    return isinstance(x, pymongo.results.DeleteResult)

def userActividad(coleccion, uid):
    """Funcion para ver si un usuario tiene actividad.

    Devuelve el numero de titulos que tiene registrados.

    Parámetros:
    coleccion -- es la coleccion que donde se hace la busqueda.
    uid -- Es el indentificador del usuario, para ver la actividad que tiene.


    """

    return coleccion.count_documents({'uid': uid})




class Test(unittest.TestCase):
    global uid
    global tipo
    global c
    uid = random.randint(10000, 100000)
    tipo = random.choice(["libro", "pelicula", "serie"])
    c = conectarColeccion(True)


    def test_A_Conectar(self):
        self.assertTrue(c ,  "Conexion DB falla")


    def test_B_Insertar(self):

        data = {'titulo': 'test prueba','año' : 2018, 'puntuacion': 10, 'tipo' : tipo, 'uid': uid}

        self.assertTrue(insertarDatos(c, data), "Inserccion incorrecta")


    def test_C_Modificar(self):
        tipo1 = random.choice(["libro", "pelicula", "serie"])
        titulo = "test prueba"
        new_datos = {'titulo': 'mod test prueba', 'año': 2017, 'puntuacion': 8, 'tipo':tipo1}

        self.assertTrue(modificarDatos(c, titulo, new_datos, uid), "Modificacion incorrecta")

    def test_D_UserActividad(self):
        #igual que antes pero se busca un uid.
        self.assertGreaterEqual(userActividad(c, uid),1, "No tiene actividad")


    def test_E_Borrar(self):
        #igual pero para borrar dato

        titulo_borrar = "mod test prueba"

        self.assertTrue(eliminarDatos(c, titulo_borrar, uid), "Borrado incorrecto")


    #liberar datos base de datos
    c.remove({})

if __name__ == '__main__':
    unittest.main()
