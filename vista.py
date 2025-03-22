from cProfile import label
import tkinter as tk
from tkinter import Menu
from logica import Producto

from setuptools import Command


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Precios para Qendra")
        self.geometry("800x600")
        self.crear_menu()

    def crear_menu(self):
        menu_principal = Menu(self)
        self.config(menu=menu_principal)

        menu_archivo = Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Cargar Archivo CSV", command=self.cargar_archivo)
        menu_archivo.add_command(label="Generar Archivo CSV", command=self.generar_archivo)
        menu_archivo.add_command(label="Salir", command=self.quit)


        menu_productos = Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Productos", menu=menu_productos)
        menu_productos.add_command(label="Listar Productos", command=self.listar_productos)
        menu_productos.add_command(label="Cargar Producto", command=self.cargar_producto)
        menu_productos.add_command(label="Borrar Producto", command=self.borrar_producto)
        menu_productos.add_command(label="Modificar Producto", command=self.modificar_producto)

        menu_proveedores = Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Proveedores", menu=menu_proveedores)
        menu_proveedores.add_command(label="Listar Proveedores",command=self.listar_proveedores)
        menu_proveedores.add_command(label="Cargar Proveedores",command=self.cargar_proveedores)
        menu_proveedores.add_command(label="Borrar Proveedores",command=self.borrar_proveedores)
        menu_proveedores.add_command(label="Modificar Proveedores",command=self.modificar_proveedores)

        menu_gestion = Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Gestión de Precios", menu=menu_gestion)
        

    def cargar_archivo(self):
        pass

    def generar_archivo(self):
        pass

    def listar_productos(self):
        pass

    def cargar_producto(self):
        formulario= PlantillaProducto(self,"Cargar Producto")
        formulario.grab_set()

    def borrar_producto(self):
        pass

    def modificar_producto(self):
        formulario = PlantillaProducto(self,"Modificar Producto","modificar")
        formulario.grab_set()

    def listar_proveedores(self):
        pass
    
    def cargar_proveedores(self):
        pass

    def borrar_proveedores(self):
        pass

    def modificar_proveedores(self):
        pass


class PlantillaProducto(tk.Toplevel):

    def __init__(self, parent,titulo,modo="guardar"):
        super().__init__(parent)
        self.title(titulo)
        self.geometry("400x300")
        
        # Campos de entrada
        tk.Label(self, text="Nombre de Sección").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nombre_de_seccion = tk.StringVar()
        self.nombre_de_seccion_entrada = tk.Entry(self, textvariable=self.nombre_de_seccion)
        self.nombre_de_seccion_entrada.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Código de PLU").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.codigo_de_PLU = tk.StringVar()
        self.codigo_de_PLU_entrada = tk.Entry(self,textvariable=self.codigo_de_PLU)
        self.codigo_de_PLU_entrada.grid(row=1, column=1, padx=10, pady=5)

        if (modo=="modificar"):
            tk.Button(self, text="Seleccionar", command=self.seleccionar_producto).grid(row=1, column=2, columnspan=2, pady=20)

        tk.Label(self, text="Descripción").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.descripcion = tk.StringVar()
        self.descripcion_entrada = tk.Entry(self,textvariable=self.descripcion)
        self.descripcion_entrada.grid(row=2, column=1, padx=10, pady=5)


        if(modo=="guardar"):
            self.producto = Producto()
            tk.Button(self, text="Guardar", command=self.guardar).grid(row=3, column=0, columnspan=2, pady=20)
        else:
            tk.Button(self, text="Modificar", command=self.modificar).grid(row=3, column=0, columnspan=2, pady=20)

    def guardar(self):        
        self.producto.asignar_valores(self)
        self.producto.guardar()

    def modificar(self):
        self.producto.asignar_valores(self)
        self.producto.modificar()

    def seleccionar_producto(self):
        self.producto= Producto(self.codigo_de_PLU.get())
        self.producto.completar_campos(self)
        




if __name__ == "__main__":
    app = App()
    app.mainloop()