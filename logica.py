from math import prod
import modelo

base = modelo.Modelo

class Producto:
    def __init__(self):
        self.nombre_de_seccion= None
        self.codigo_de_PLU= None
        self.descripcion= None
        self.numero_de_PLU= None
        self.precio_lista_1= None
        self.precio_lista_2 = None
        self.tipo_de_venta= None
        self.vencimiento= None
        self.otros_datos= None
        self.tara= None
        self.porcentaje_de_agua= None
        self.origen= None
        self.datos_de_conservacion= None
        self.recetas_de_ingredientes= None
        self.tabla_nutricional= None
        self.porcion= None
        self.calorias_por_porcion= None
        self.carbohidratos= None
        self.proteinas= None
        self.grasas_totales= None
        self.grasas_saturadas= None
        self.grasas_trans= None
        self.fibra= None
        self.sodio= None
        self.configuracion_EAN= None
        self.descripcion_EAN= None

    def cargar_desde_DB(self,id):
        producto = base.seleccionar("Productos", "*", "id = ",id)
        producto[0][0] = self.nombre_de_seccion
        producto[0][1] = self.codigo_de_PLU
        producto[0][2]= self.descripcion
        producto[0][3]= self.numero_de_PLU
        producto[0][4]= self.precio_lista_1
        producto[0][5]= self.precio_lista_2
        producto[0][6]= self.tipo_de_venta
        producto[0][7]= self.vencimiento
        producto[0][8]=self.otros_datos
        producto[0][9]=self.tara
        producto[0][10]=self.porcentaje_de_agua
        producto[0][11]=self.origen
        producto[0][12]=self.datos_de_conservacion
        producto[0][13]=self.recetas_de_ingredientes
        producto[0][14]=self.tabla_nutricional
        producto[0][15]=self.porcion
        producto[0][16]=self.calorias_por_porcion
        producto[0][17]=self.carbohidratos
        producto[0][18]=self.proteinas
        producto[0][19]=self.grasas_totales
        producto[0][20]=self.grasas_saturadas
        producto[0][21]=self.grasas_trans
        producto[0][22]=self.fibra
        producto[0][23]=self.sodio
        producto[0][24]=self.configuracion_EAN
        producto[0][25]=self.descripcion_EAN

        




