import sqlite3

class   conexion:
    def __init__(self):
        self.base_datos = "DATABASE/BDhistorial.db"
        self.conexionBD = sqlite3.connect(self.base_datos)
        self.cursor = self.conexionBD.cursor()

    def cerrar_conexion(self):
        self.conexionBD.commit()
        self.conexionBD.close()