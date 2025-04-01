from math import prod
from pickle import FALSE, TRUE
from modelo import Modelo

base = Modelo("database.db")

class Entidad:

    #se asignan los atributos de manera dinámica, usando los nombres de los campos de la tabla
    def __init__(self,tabla,campo_clave, id=None, lista_de_campos=None,lista_de_valores=None):
        self.tabla = tabla
        self.campo_clave = campo_clave
        self.id = id 
        #La lista de campos y valores vienen como argumento cuando es para una lista de objetos
        #de manera que no tenga que consultar a la base con cada construcción
        if (lista_de_campos is not None):
            self.lista_de_campos = lista_de_campos
        elif(id is not None):
            self.lista_de_campos = base.obtener_campos(tabla)
            lista_de_valores = base.seleccionar(tabla, "*", f"{campo_clave} = ?",[id])[0]
        else:
            self.lista_de_campos = base.obtener_campos(tabla)

        if (id is None and lista_de_valores is None):
            for campo in self.lista_de_campos:
                setattr(self,campo,None)
        else:
            for campo, valor in zip(self.lista_de_campos,lista_de_valores):
                setattr(self,campo,valor)


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

    def guardar(self):
        valores = []
        campos = []
        for campo in self.lista_de_campos:
            valor = getattr(self,campo,None)
            if(campo != self.campo_clave):
                valores.append(valor)
                campos.append(campo)
            elif(valor is not None):
                if(base.contar_registros(self.tabla,self.campo_clave,valor) == 0 ):
                    valores.append(valor)
                    campos.append(campo)
                else:
                    return False #si ya un registro con ese id
        base.insertar(self.tabla,campos,valores)
        return True
    
    #Asigna los valores de los campos de un formulario a los atributos del objeto
    def asignar_valores(self,formulario):    
        for campo in self.lista_de_campos:
            valor = getattr(formulario, campo,None)
            if (valor is not None):
                valor = valor.get()
                setattr(self,campo,valor)

    #completa los inputs de un formulario con los valores de los atributos del objeto
    def completar_campos(self,formulario):
        for campo in self.lista_de_campos:
            variable_input= getattr(formulario, campo, None)
            if (variable_input is not None):
                valor=getattr(self,campo)
                variable_input.set(valor)

    def obtener_valor(self,campo):
        return getattr(self,campo)
        
            

class Lista:
    def __init__(self,tabla,clase_objeto,condicion=None,valores=None):
        matriz = base.seleccionar(tabla,"*",condicion,valores)
        campos = base.obtener_campos(tabla)
        self.lista = []
        for registro in matriz:
            self.lista.append(clase_objeto(lista_de_campos=campos,lista_de_valores=registro))

    def listar_columnas(self,columnas):
        valores= []
        for linea in self.lista:
            if len(columnas)!= 1:
                valor = []
                for columna in columnas:
                    valor.append(getattr(linea, columna, None))
            else:
                valor = getattr(linea, columnas[0],None)
            valores.append(valor)
        print (valores)
        return valores




class Producto(Entidad):
    def __init__(self, id=None,lista_de_campos=None,lista_de_valores=None):
        super().__init__("Productos","codigo_de_PLU", id,lista_de_campos,lista_de_valores)

class ListaProductos (Lista):
    def __init__(self,condicion=None,valores=None):
        super().__init__("Productos",Producto,condicion,valores)

class Seccion(Entidad):
    def __init__(self, id=None, lista_de_campos=None, lista_de_valores=None):
        super().__init__("Secciones", "id", id, lista_de_campos, lista_de_valores)

class ListaSecciones(Lista):
    def __init__(self, condicion=None, valores=None):
        super().__init__("Secciones", Seccion, condicion, valores)


