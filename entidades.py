import ABM_MVC.controlador as controlador


controlador.pasar_ubicacion_db("database.db")

class Producto(controlador.Entidad):
    tabla = "Productos"
    campo_clave = "codigo_de_PLU"


class Seccion(controlador.Entidad):
    tabla = "Secciones"
    campo_clave= "id"


controlador.registrar_entidades((Producto,Seccion))



