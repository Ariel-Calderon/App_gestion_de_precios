import entidades
from ABM_MVC.vista import Formulario_ABM,Formulario_CSV

class ABM_Producto(Formulario_ABM):  
    def __init__(self, parent,titulo,modo="guardar"):
        super().__init__(parent,entidades.Producto,modo)
        self.title(titulo)
        self.geometry("400x300")   

        self.crear_combobox(True,"Sección","Secciones")
        self.crear_entry(True,"Código de PLU","codigo_de_PLU","enteros")
        self.crear_entry(True, "Descripción","descripcion")

        self.render_formulario_ABM()          

class ABM_Seccion(Formulario_ABM):
    def __init__(self, parent,titulo,modo="guardar"):
        super().__init__(parent,entidades.Seccion,modo)
        self.title(titulo)
        self.geometry("400x300")     

        self.crear_combobox(False,"Sección","id") #no es obligatorio cuando el id es autoincrement en la base
        self.crear_entry(True,"Descripción", "descripcion")
        self.crear_entry(False,"Porcentaje de Ganancia", "porcentaje_ganancia","decimales")

        self.render_formulario_ABM()

class Gestion_Archivos_CSV(Formulario_CSV):
    def __init__(self,  modo="cargar"): 
        super().__init__( entidades.Producto, modo) 
        

