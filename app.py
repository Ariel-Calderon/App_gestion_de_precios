from vistas import ABM_Producto, ABM_Seccion, Gestion_Archivos_CSV
from tkinter import Menu
import tkinter as tk

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

        menu_secciones = Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Secciones", menu=menu_secciones)
        menu_secciones.add_command(label="Listar Secciones",command=self.listar_secciones)
        menu_secciones.add_command(label="Cargar Secciones",command=self.cargar_secciones)
        menu_secciones.add_command(label="Borrar Secciones",command=self.borrar_secciones)
        menu_secciones.add_command(label="Modificar Secciones",command=self.modificar_secciones)

        menu_proveedores = Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Proveedores", menu=menu_proveedores)
        menu_proveedores.add_command(label="Listar Proveedores",command=self.listar_proveedores)
        menu_proveedores.add_command(label="Cargar Proveedores",command=self.cargar_proveedores)
        menu_proveedores.add_command(label="Borrar Proveedores",command=self.borrar_proveedores)
        menu_proveedores.add_command(label="Modificar Proveedores",command=self.modificar_proveedores)

        menu_gestion = Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Gestión de Precios", menu=menu_gestion)
        

    def cargar_archivo(self):
        Gestion_Archivos_CSV() 
        

    def generar_archivo(self):
        pass

    def listar_productos(self):
        pass

    def cargar_producto(self):
        formulario= ABM_Producto(self,"Cargar nuevo producto")
        formulario.grab_set()

    def borrar_producto(self):
        pass

    def modificar_producto(self):
        formulario = ABM_Producto(self,"Modificar un producto","modificar")
        formulario.grab_set()

    def listar_secciones(self):
        pass

    def cargar_secciones(self):
        formulario=ABM_Seccion(self,"Cargar nueva sección")
        formulario.grab_set()

    def borrar_secciones(self):
        pass

    def modificar_secciones(self):
        formulario=ABM_Seccion(self,"Modificar una Sección","modificar")
        formulario.grab_set()

    def listar_proveedores(self):
        pass
    
    def cargar_proveedores(self):
        pass

    def borrar_proveedores(self):
        pass

    def modificar_proveedores(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
