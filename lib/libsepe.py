class libsepe:
    def __init__(self):
        super().__init__()
    ### La coleccionira de la forma::
    ##  {uid: [<contenido>], uid2: [<contenido>]}
    # En contenido ira lo que el usuario a visto
    global coleccion
    coleccion={}
    def crear_dato(titulo, año, punt,tipo):
        return [{'titulo':titulo, 'año': año, 'mi_puntuacion': punt,'tipo':tipo}]

    def insertarDatos(datos,uid):
        """Funcion para insertar datos en la colleccion donde va almacenado todo.

        Devuelve True si se ha insertado correctamente y se crea una instancia de
        InsertOneResult, en caso contrario False.

        Parámetros:
        datos -- Los datox que el usuario introduce.
        uid -- el indentificador del usuario.

        """
        if uid in coleccion:
            coleccion[uid].append(datos)
        else:
            coleccion[uid] = datos

        if uid in coleccion:
            return True
        else:
            return False

    def modificarDatos(titulo, new_datos, uid):
        """Funcion para modificar datos de la colleccion donde va almacenado todo.

        Devuelve True si se ha modificado correctamente y se crea una instancia de
        UpdateResult, en caso contrario False.

        Parámetros:
        titulo -- Es el titulo exacto, igual que esta en la colleccion, del dato que
            se quiere modifcar. Se puede modificar el titulo también si así se quisiera.
        new_datos -- es un diccionario donde estan los nuevos datos.
        uid -- Es el indentificador del usuario, para poder modificar un valor debe
            coincidir el titulo y el uid. Este valor es el unico que no se puede modificar.

        """

        if uid in coleccion:
            for it in coleccion[uid]:
                if it['titulo'] == titulo:
                    reg_mod=it
            index=coleccion[uid].index(reg_mod)
            coleccion[uid][index]=new_datos

            return True
        else:
            return False

    def eliminarDatos(titulo, uid):
        """Funcion para eliminar datos de la colleccion donde va almacenado todo.

        Devuelve True si se ha eliminado correctamente y se crea una instancia de
        DeleteResult, en caso contrario False.

        Parámetros:
        titulo -- Es el titulo exacto, igual que esta en la coleccion, del dato que
            se quiere eliminar.
        uid -- Es el indicador del usuario, para poder eliminar un valor debe
            coincidir el titulo y el uid.


        """


        if uid in coleccion:
            reg_antes=libsepe.userActividad(uid)
            for it in coleccion[uid]:
                if it['titulo'] == titulo:
                    reg_mod=it
            index=coleccion[uid].index(reg_mod)
            coleccion[uid].pop(index)
            if reg_antes-1 == libsepe.userActividad(uid):
                return True
            else:
                return False
        else:
            return False

    def userActividad( uid):
        """Funcion para ver si un usuario tiene actividad.

        Devuelve el numero de titulos que tiene registrados.

        Parámetros:
        uid -- Es el indentificador del usuario, para ver la actividad que tiene.


        """
        cont=0
        if uid in coleccion:
            for it in coleccion[uid]:
                cont+=1


        return cont
