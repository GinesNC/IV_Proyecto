import unittest
import pymongo

def conectarDB():
    try:
        conn=pymongo.MongoClient('localhost', 27017)
        print("Connected successfully!!!")
    except(pymongo.errors.ConnectionFailure, e):
        print("Could not connect to MongoDB: %s") % e
    return conn['lsp_db']

def insert_data(type, data, uid):
    #insertar en base de datos #si x es una instancia de insertoneresult es que si se ha insertado.



    return isinstance(x, pymongo.results.InsertOneResult)


def modify_data(title, new_data, uid):
    # se modifica y se busca por titulo (lo ideal seria añadir un id unico)
    # igual que antes pero con la clase updateresult
def delete_data(id):
    #cuando en el bot se elige eliminar devuelve la peli que es buscada por tituloself.
    #cuando la encuentra la mustra y pide la confirmacion del ususario. Si le da a si
    #se llama a esta funcion y se le pasa el identificador unico. el id no se muestra.
    # tb devuelve una instancia de deleteresult

def user_activity(uid):
    # esto devuelve si el usuario tiene alguna actividad. si es asi devuelve el numero
    # de libros pelis y series que tieneself.

def nota(titulo):
    #ayudanmoe de enlace_nota.py


class Test(unittest.TestCase):

    def testConectar(self):
        self.assertEqual(conectarDB(), "Connected successfully!!!", "Conexion DB OK")

    #se crea un uid al azar, se conecta a la base de datos y se crea una colleccion de prueba
    # para comprobar que se realizan las acciones de la base de datos correctamente.
    uid = round
    db = conectarDB()
    columna = db['test_pruebas']

    def testInsert(self):
        type = round{peli,libro,series}
        data = {aaaaaaa, 1234, 9}


        x = columna.insert_one(data)


        #si es igual el print a los datos insertados pasa el test.
        self.assertTrue(insert_data(type, data, uid), "Inserccion correcta")


    def testModyfy(self):
        #igual que antes pero para modificar
        type = round{peli,libro,series}
        title = "aaaaaaaaaaaa"
        data_nuew


        x = columna.(data)


        #si es igual el print a los datos insertados pasa el test.
        self.assertTrue(modify_data(title, data_new, uid), "Modificacion correcta")

    def testDelete(self):
        #igual pero para borrar dato

        data_borrar = #por ejemplo un id o el titulo para buscar.

        self.assertTrue(delete_data(id), "Borrado correcto")


    def testActivity(self):
        #igual que antes pero se busca un uid.

        self.assertTrue(user_activity(uid), "Comprobacion de actividad correcta")


    def testObtenerNota(self):
        # Para que este entre 0 y 10, se cumple el test
        self.assertTrue(nota(title), "obtencion correcta")



    #liberar datos base de datos

if __name__ == '__main__':
    unittest.main()
