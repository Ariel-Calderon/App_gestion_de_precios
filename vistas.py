import entidades
from ABM_MVC.vista import Plantilla

class PlantillaProducto(Plantilla):
    

    def __init__(self, parent,titulo,modo="guardar"):
        super().__init__(parent,entidades.Producto,modo)
        self.title(titulo)
        self.geometry("400x300")   

        self.crear_combobox(True,"Sección","Secciones")
        self.crear_entry(True,"Código de PLU","codigo_de_PLU","enteros")
        self.crear_entry(True, "Descripción","descripcion")

        self.render_formulario_ABM()  
            


   

class PlantillaSeccion(Plantilla):

    def __init__(self, parent,titulo,modo="guardar"):
        super().__init__(parent,entidades.Seccion,modo)
        self.title(titulo)
        self.geometry("400x300")     

        self.crear_combobox(False,"Sección","id") #no es obligatorio cuando el id es autoincrement en la base
        self.crear_entry(True,"Descripción", "descripcion")
        self.crear_entry(False,"Porcentaje de Ganancia", "porcentaje_ganancia","decimales")

        self.render_formulario_ABM()


class PlantillaCSV(Plantilla):
    def __init__(self, parent, modo="guardar"):
        super().__init__(parent, entidades.Producto, modo)
        self.title("Cargar archivo CSV")
        self.geometry("400x300")

        self.render_formulario_CSV()
