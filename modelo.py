import sqlite3

class Modelo:
    def __init__(self, db_path="database.db"):       
        self.db_path = db_path

    def abrir_conexion(self):
        return sqlite3.connect(self.db_path)

    def ejecutar_consulta(self, query, params=None, fetchall=True):        
        conexion = self.abrir_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(query, params or [])
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall() if fetchall else cursor.fetchone()
            else:
                conexion.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            print(f"Error en la consulta SQL: {e}")
            return None
        finally:
            conexion.close()

    def crear_tabla(self, tabla, esquema):
        query = f"CREATE TABLE IF NOT EXISTS {tabla} ({esquema})"
        self.ejecutar_consulta(query)

    def insertar(self, tabla, columnas, valores):        
        placeholders = ", ".join(["?"] * len(valores))
        columnas_str = ", ".join(columnas)
        query = f"INSERT INTO {tabla} ({columnas_str}) VALUES ({placeholders})"
        conexion = self.abrir_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(query, valores)
            conexion.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error al insertar en la tabla {tabla}: {e}")
            return None
        finally:
            conexion.close()

    def actualizar(self, tabla, columnas, valores, condicion):
        set_clause = ", ".join([f"{col} = ?" for col in columnas])
        query = f"UPDATE {tabla} SET {set_clause} WHERE {condicion}"
        return self.ejecutar_consulta(query, valores, fetchall=False)

    def eliminar(self, tabla, condicion, valores):
        query = f"DELETE FROM {tabla} WHERE {condicion}"
        return self.ejecutar_consulta(query, valores, fetchall=False)

    def seleccionar(self, tabla, columnas="*", condicion=None, valores=None):
        query = f"SELECT {columnas} FROM {tabla}"
        if condicion:
            query += f" WHERE {condicion}"
        return self.ejecutar_consulta(query, valores)
    
    def obtener_campos(self,tabla):
        conexion = self.abrir_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(f"PRAGMA table_info ({tabla})")
            lista_de_campos = []
            for fila in cursor.fetchall():
                lista_de_campos.append(fila[1])                
            return lista_de_campos
        finally:
            conexion.close()

    def contar_registros(self,tabla,campo,valor):
        conexion = self.abrir_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(F"SELECT COUNT (*) FROM {tabla} WHERE {campo} = {valor}")
            return cursor.fetchall()[0][0]
        finally:
            conexion.close()
