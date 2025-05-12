import ABM_MVC.controlador as controlador


controlador.pasar_ubicacion_db("database.db")


class Producto(controlador.Entidad):
    tabla = "Productos"
    campo_clave = "codigo_de_PLU"


class Seccion(controlador.Entidad):
    tabla = "Secciones"
    campo_clave= "id"


controlador.registrar_entidades((Producto,Seccion))



"""
cargarArchivo = controlador.ArchivoCsv(Producto)
cargarArchivo.abrir_archivo("datos.csv")
print(cargarArchivo.lista_contenido)
cargarArchivo.crear_lista_de_objetos()

cargarArchivo.guardar_lista_de_objetos()
"""
