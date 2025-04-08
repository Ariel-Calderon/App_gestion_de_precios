from math import prod
from pickle import FALSE, TRUE
from modelo import Modelo

base = Modelo("database.db")

class Entidad:

    #se asignan los atributos de manera dinámica, usando los nombres de los campos de la tabla
    def __init__(self, id=None, lista_de_campos=None,lista_de_valores=None):
        self.tabla = self.__class__.tabla
        self.campo_clave = self.__class__.campo_clave
        self.id = id 
        #La lista de campos y valores vienen como argumento cuando es para una lista de objetos
        #de manera que no tenga que consultar a la base con cada construcción
        if (lista_de_campos is not None):
            self.lista_de_campos = lista_de_campos
        elif(id is not None):
            self.lista_de_campos = base.obtener_campos(self.tabla)
            lista_de_valores = base.seleccionar(self.tabla, "*", f"{self.campo_clave} = ?",[id])[0]
        else:
            self.lista_de_campos = base.obtener_campos(self.tabla)

        if (id is None and lista_de_valores is None):
            for campo in self.lista_de_campos:
                setattr(self,campo,None)
        else:
            for campo, valor in zip(self.lista_de_campos,lista_de_valores):
                setattr(self,campo,valor)

    @classmethod
    def ver_parametros(cls): 
        print (cls.tabla)
        print (cls.campo_clave)       
        return [cls.tabla,cls.campo_clave]

    def borrar(self):
        base.eliminar(self.tabla,f"{self.campo_clave} = ?",[self.id])

    def modificar(self):
        valores = []
        campos_sin_id = []
        for campo in self.lista_de_campos:
            if (campo != self.campo_clave):
                campos_sin_id.append(campo)
                valores.append(getattr(self,campo,None))
        return base.actualizar(self.tabla,campos_sin_id,valores,f" {self.campo_clave} = {self.id}")

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
                    return [False, "Ya existe un registro con la misma clave"] #si ya un registro con ese id
        id_insertado = base.insertar(self.tabla,campos,valores)
        if id_insertado is not None:
            return [True, "El registro ha sido guardado exitosamente.",id_insertado]
        else:
            return [False, "Error al intentar guardar el registro"]
    
    #Asigna los valores de los campos de un formulario a los atributos del objeto
    def asignar_valores(self,formulario):    
        for campo in self.lista_de_campos:
            atributo = getattr(formulario, campo,None)
            if (atributo is not None):
                valor = atributo.get()
                setattr(self,campo,valor)
        if (formulario.lista_de_comboboxes is not None):
            for combo in formulario.lista_de_comboboxes:
                valor = combo[2][combo[0].current()]
                setattr(self,combo[1],valor)

    #completa los inputs de un formulario con los valores de los atributos del objeto
    def completar_campos(self,formulario):
        for campo in self.lista_de_campos:
            variable_input= getattr(formulario, campo, None)
            if (variable_input is not None):
                valor=getattr(self,campo)
                variable_input.set(valor)
        if formulario.lista_de_comboboxes is not None:
            for combo in formulario.lista_de_comboboxes:
                id = getattr(self,combo[1])
                indice = 0
                for clave in combo[2]:
                    if clave == id:
                        break
                    indice += 1
                combo[0].current(indice)

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
        return valores




class Producto(Entidad):
    tabla = "Productos"
    campo_clave = "codigo_de_PLU"
  #  def __init__(self, id=None,lista_de_campos=None,lista_de_valores=None):
  #      super().__init__("Productos","codigo_de_PLU", id,lista_de_campos,lista_de_valores)

class ListaProductos (Lista):
    def __init__(self,condicion=None,valores=None):
        super().__init__("Productos",Producto,condicion,valores)

class Seccion(Entidad):
    tabla = "Secciones"
    campo_clave= "id"
#    def __init__(self, id=None, lista_de_campos=None, lista_de_valores=None):
#        super().__init__("Secciones", "id", id, lista_de_campos, lista_de_valores)

class ListaSecciones(Lista):
    def __init__(self, condicion=None, valores=None):
        super().__init__("Secciones", Seccion, condicion, valores)


