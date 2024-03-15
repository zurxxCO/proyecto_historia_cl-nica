from .conexionBD import conexion
from sqlite3 import Error as SQLiteError
from tkinter import messagebox


def editarDatoPaciente(persona, idPersona):
    conexionBD = conexion()
    sql = f"""UPDATE Persona SET nombre = '{persona.nombre}', apellidoPaterno = '{persona.apellidoPaterno}', apellidoMaterno = '{persona.apellidoMaterno}', 
    documentoIdentidad = '{persona.documentoIdentidad}', fechaNacimiento = '{persona.fechaNacimiento}', 
    edad = '{persona.edad}', antecedentes = '{persona.antecedentes}', correoElectronico = '{persona.correoElectronico}',
    direccionResidencia = '{persona.direccionResidencia}', telefono = '{persona.telefono}', activo = 1 WHERE idPersona = {idPersona}"""

    try:
        conexionBD.cursor.execute(sql)
        conexionBD.cerrar_conexion()
        title = "EDITAR PACIENTE"
        mensaje = "Actualización Exitosa"
        messagebox.showinfo(title, mensaje)
    except:
        title = "EDITAR PACIENTE"
        mensaje = "Error al Actualizar"
        messagebox.showinfo(title, mensaje)


def guardarDatosPaciente(Persona):
    conexionBD = conexion()
    sql = f"""INSERT INTO persona (nombre, apellidoPaterno, apellidoMaterno, documentoIdentidad, fechaNacimiento, edad,
                 antecedentes, correoElectronico, direccionResidencia, telefono, activo) VALUES('{Persona.nombre}', '{Persona.apellidoPaterno}',
                 '{Persona.apellidoMaterno}', '{Persona.documentoIdentidad}', '{Persona.fechaNacimiento}', '{Persona.edad}',
                 '{Persona.antecedentes}', '{Persona.correoElectronico}', '{Persona.direccionResidencia}', '{Persona.telefono}', 1)"""
    
    try:
        conexionBD.cursor.execute(sql)
        conexionBD.cerrar_conexion()
        title = "REGISTRO DE PACIENTE"
        mensaje = "Registro Exitoso"
        messagebox.showinfo(title, mensaje)
        
    except SQLiteError as e: 
        title = "REGISTRO DE PACIENTE"
        mensaje = f"Error de registro: {str(e)}"
        messagebox.showerror(title, mensaje)


def listar():
    conexionBD = conexion()

    listaPersona=[]
    sql = "SELECT * FROM Persona WHERE ACTIVO = 1"

    try:
        conexionBD.cursor.execute(sql)
        listaPersona = conexionBD.cursor.fetchall()
        conexionBD.cerrar_conexion()
    except:
        title = "DATOS"
        mensaje = "Registro no Existente" 
        messagebox.showwarning(title, mensaje)
    return listaPersona
    

def listarCondicion(where):
    conexionBD = conexion()
    
    listaPersona=[]
    sql = f"SELECT * FROM Persona {where}"
    
    try:
        conexionBD.cursor.execute(sql)
        listaPersona = conexionBD.cursor.fetchall()
        conexionBD.cerrar_conexion()
    
    except SQLiteError as e:
        title = "DATOS"
        mensaje = f"Registro no Existente: {str(e)}" 
        messagebox.showwarning(title, mensaje)
    return listaPersona

def eliminarPaciente(idPersona):
    conexionBD = conexion()

    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""

    try:
        conexionBD.cursor.execute(sql)
        conexionBD.cerrar_conexion()
        title = "ELIMINAR PACIENTE"
        mensaje = "Paciente Eliminado Satisfactoriamente" 
        messagebox.showwarning(title, mensaje)
    except:
        title = "ELIMINAR PACIENTE"
        mensaje = "No se Pudo Eliminar el Registro" 
        messagebox.showwarning(title, mensaje)



class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, documentoIdentidad, fechaNacimiento, edad,
                 antecedentes, correoElectronico, direccionResidencia, telefono):
        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.documentoIdentidad = documentoIdentidad
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correoElectronico = correoElectronico
        self.direccionResidencia = direccionResidencia
        self.telefono = telefono

    def __str__(self):
        return f"""persona[{self.nombre}, {self.apellidoPaterno}, {self.apellidoMaterno}, {self.documentoIdentidad}, {self.fechaNacimiento}, {self.edad}, {self.antecedentes}, {self.correoElectronico}, {self.direccionResidencia}, {self.telefono}]"""