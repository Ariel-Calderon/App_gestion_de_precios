import sys
import ABM_MVC.controlador as controlador


controlador.Entidad.pasar_ubicacion_modulo(sys.modules[__name__])
controlador.pasar_ubicacion_db("database.db")


class Producto(controlador.Entidad):
    tabla = "Productos"
    campo_clave = "codigo_de_PLU"

class ListaProductos (controlador.Lista): 
    def __init__(self,condicion=None,valores=None):
        super().__init__("Productos",Producto,condicion,valores)

class Seccion(controlador.Entidad):
    tabla = "Secciones"
    campo_clave= "id"

class ListaSecciones(controlador.Lista):  
    def __init__(self, condicion=None, valores=None):
        super().__init__("Secciones", Seccion, condicion, valores)