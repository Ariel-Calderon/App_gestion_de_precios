from math import prod
from modelo import Modelo

base = Modelo("database.db")

class Producto:

    #se asignan los atributos de manera dinámica, usando los nombres de los campos de la tabla
    def __init__(self,id):
        lista_de_campos = base.obtener_campos("Productos")
        valores = base.seleccionar("Productos", "*", "codigo_de_PLU = ?",[id])[0]
        for campo, valor in zip(lista_de_campos,valores):
            setattr(self,campo,valor)
            
    def imprimir (self):
        print (self.descripcion)


articulo = Producto(29)
#articulo.cargar_desde_DB(29)
articulo.imprimir()

