from math import prod
from modelo import Modelo

base = Modelo("database.db")

class Entidad:

    #se asignan los atributos de manera dinámica, usando los nombres de los campos de la tabla
    def __init__(self,tabla,campo_clave, id=None):
        self.tabla = tabla
        self.campo_clave = campo_clave
        self.id = id 
        self.lista_de_campos = base.obtener_campos(tabla)
        if (id is not None):
            valores = base.seleccionar(tabla, "*", f"{campo_clave} = ?",[id])[0]
            for campo, valor in zip(self.lista_de_campos,valores):
                setattr(self,campo,valor)
        else:
            for campo in self.lista_de_campos:
                setattr(self,campo,None)

    def borrar(self):
        base.eliminar(self.tabla,f"{self.campo_clave} = ?",[self.id])

    def modificar(self):
        valores = []
        campos_sin_id = []
        for campo in self.lista_de_campos:
            if (campo != self.campo_clave):
                campos_sin_id.append(campo)
                valores.append(getattr(self,campo,None))
        base.actualizar(self.tabla,campos_sin_id,valores,f" {self.campo_clave} = {self.id}")



class Producto(Entidad):

    def __init__(self, id=None):
        super().__init__("Productos","codigo_de_PLU", id)

    def imprimir (self):
        print (self.descripcion)


articulo = Producto(29)
articulo.imprimir()
articulo.descripcion = "prueba modificacion"
articulo.modificar()


