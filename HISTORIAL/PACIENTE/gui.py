import tkinter as tk
import tkcalendar as tc
from tkinter import*
from tkinter import ttk, Entry, Label, scrolledtext, StringVar, Toplevel
from tkinter import messagebox
from MODELO.infoDao import Persona, guardarDatosPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date



class Frame(tk.Frame):
    def __init__(self, ventanaprincipal):
        super().__init__(ventanaprincipal, width=1280, height=720)
        
        self.ventanaprincipal=ventanaprincipal
        self.pack()
        self.config(bg="#5B792D")
        self.idPersona = None
        self.Campos_Paciente()
        self.deshabilitar_campos()
        self.tablaPaciente()


    def Campos_Paciente(self):

        #LABELS
        self.lblnombre=tk.Label(self, text="Nombre:")
        self.lblnombre.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lblnombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblapepater=tk.Label(self, text="Primer Apellido:")
        self.lblapepater.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lblapepater.grid(column=0, row=1, padx=10, pady=5)

        self.lblapemater=tk.Label(self, text="Segundo Apellido:")
        self.lblapemater.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lblapemater.grid(column=0, row=2, padx=10, pady=5)

        self.lbldni=tk.Label(self, text="Documento de Identidad:")
        self.lbldni.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lbldni.grid(column=0, row=3, padx=10, pady=5)

        self.lblnacimiento=tk.Label(self, text="Fecha de Nacimiento:")
        self.lblnacimiento.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lblnacimiento.grid(column=0, row=4, padx=10, pady=5)

        self.lbledad=tk.Label(self, text="Edad:")
        self.lbledad.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lbledad.grid(column=0, row=5, padx=10, pady=5)

        self.lblantecedentes=tk.Label(self, text="Antecedentes:")
        self.lblantecedentes.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lblantecedentes.grid(column=0, row=6, padx=10, pady=5)

        self.lblcorreo=tk.Label(self, text="E-mail:")
        self.lblcorreo.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lblcorreo.grid(column=0, row=7, padx=10, pady=5)

        self.lbldireccion=tk.Label(self, text="Dirección:")
        self.lbldireccion.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lbldireccion.grid(column=0, row=8, padx=10, pady=5)

        self.lbltelefono=tk.Label(self, text="Teléfono:")
        self.lbltelefono.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lbltelefono.grid(column=0, row=9, padx=10, pady=5)

        #CAJAS DE TEXTO
        self.svnombre = tk.StringVar()
        self.entrynombre = tk.Entry(self, textvariable = self.svnombre)
        self.entrynombre.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entrynombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svapepater = tk.StringVar()
        self.entryapepater = tk.Entry(self, textvariable = self.svapepater)
        self.entryapepater.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entryapepater.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svapemater = tk.StringVar()
        self.entryapemater = tk.Entry(self, textvariable = self.svapemater)
        self.entryapemater.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entryapemater.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svdni = tk.StringVar()
        self.entrydni = tk.Entry(self, textvariable = self.svdni)
        self.entrydni.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entrydni.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svnacimiento = tk.StringVar()
        self.entrynacimiento = tk.Entry(self, textvariable = self.svnacimiento)
        self.entrynacimiento.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entrynacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svedad = tk.StringVar()
        self.entryedad = tk.Entry(self, textvariable = self.svedad)
        self.entryedad.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entryedad.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svantecedentes = tk.StringVar()
        self.entryantecedentes = tk.Entry(self, textvariable = self.svantecedentes)
        self.entryantecedentes.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entryantecedentes.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svcorreo = tk.StringVar()
        self.entrycorreo = tk.Entry(self, textvariable = self.svcorreo)
        self.entrycorreo.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entrycorreo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svdireccion = tk.StringVar()
        self.entrydireccion = tk.Entry(self, textvariable = self.svdireccion)
        self.entrydireccion.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entrydireccion.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        self.svtelefono = tk.StringVar()
        self.entrytelefono = tk.Entry(self, textvariable = self.svtelefono)
        self.entrytelefono.config(width=60, font=("Book Antiqua", 11), bg="#C7C166", fg="#091401")
        self.entrytelefono.grid(column=1, row=9, padx=10, pady=5, columnspan=2)


        #BOTONES DE COMANDO
        self.btn_nuevo = tk.Button(self, text="NUEVO", command = self.habilitar_campos)
        self.btn_nuevo.config(width=20, bg="#B7E219", activebackground="#455212", font=("Mongolian Baiti", 13, "bold"), cursor="hand2")
        self.btn_nuevo.grid(column=0, row=10, padx=15, pady=5)

        self.btn_guardar = tk.Button(self, text="GUARDAR", command=self.guardarPaciente)
        self.btn_guardar.config(width=20, bg="#4EC5F1", activebackground="#0A555B", font=("Mongolian Baiti", 13, "bold"), cursor="hand2")
        self.btn_guardar.grid(column=1, row=10, padx=15, pady=5)

        self.btn_cancelar = tk.Button(self, text="CANCELAR", command=self.deshabilitar_campos)
        self.btn_cancelar.config(width=20, bg="#F94E4B", activebackground="#9B1C1A", font=("Mongolian Baiti", 13, "bold"), cursor="hand2")
        self.btn_cancelar.grid(column=2, row=10, padx=15, pady=5)


        #BUSCADOR DE PACIENTES
        #LABEL BUSCADOR
        self.lblBuscadorCC = tk.Label(self, text= "Buscar Cédula del Paciente:")
        self.lblBuscadorCC.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lblBuscadorCC.grid(row=1, column=3, padx=10, pady=5)

        self.lblBuscadorApell = tk.Label(self, text= "Buscar Apellido del Paciente:")
        self.lblBuscadorApell.config(font=("Bell MT", 11, "bold"), bg="#5B792D")
        self.lblBuscadorApell.grid(row=2, column=3, padx=10, pady=5)


        #ENTRYS BUSCADOR
        self.svBuscadorCC = tk.StringVar()
        self.entryBuscadorCC = tk.Entry(self, textvariable=self.svBuscadorCC)
        self.entryBuscadorCC.config(width=30, font=("Book Antiqua", 12, "bold"), bg="#A98841", fg="#091401")
        self.entryBuscadorCC.grid(column=4, row=1, padx=10, pady=5)

        self.svBuscarApe = tk.StringVar()
        self.entryBuscadorApe = tk.Entry(self, textvariable=self.svBuscarApe)
        self.entryBuscadorApe.config(width=30, font=("Book Antiqua", 12, "bold"), bg="#A98841", fg="#091401")
        self.entryBuscadorApe.grid(column=4, row=2, padx=10, pady=5)

        #BOTONES BUSCADORES
        #BOTÓN
        self.btnBuscar = tk.Button(self, text="BUSCAR PACIENTE", command=self.buscarPacienteCondi)
        self.btnBuscar.config(width=18, bg="#000003", fg="#FFFFFF", activebackground="#3E3E44", font=("Mongolian Baiti", 12), cursor="hand2")
        self.btnBuscar.grid(column=4, row=3, padx=5, pady=5)

        self.btnLimpiarBuscador = tk.Button(self, text="LIMPIAR", command=self.LimpiarBusqueda)
        self.btnLimpiarBuscador.config(width=18, bg="#000003", fg="#FFFFFF", activebackground="#3E3E44", font=("Mongolian Baiti", 12), cursor="hand2")
        self.btnLimpiarBuscador.grid(column=4, row=4, padx=5, pady=5)

        #BOTÓN CALENDARIO
        self.btncalendario = tk.Button(self, text="CALENDARIO", command=self.vistaCalendario)
        self.btncalendario.config(width=14, bg="#332EDF", fg="#000000", activebackground="#170465", font=("Mongolian Baiti", 10), cursor="hand2")
        self.btncalendario.grid(column=3, row=4, padx=5, pady=5, columnspan=1)

    def vistaCalendario(self):
        self.calendario = Toplevel()
        self.calendario.title("FECHA DE NACIMIENTO")
        self.calendario.resizable(0,0)
        self.calendario.config(bg="#64AFF5")

        self.svCalendario = StringVar()
        self.svCalendario.set(datetime.now().strftime("%d/%m/%Y"))

        self.calendar = tc.Calendar(self.calendario, selectmode='day', year=1900, month=1, day=1, locale="es_US", bg="#AD7307", fg="#FFFFFF", headersbackground="#25F392", textvariable=self.svCalendario, date_pattern="dd/mm/Y")
        self.calendar.pack(pady=25)
        self.calendar.grid(row=1, column=0)
       
        #TRACE PARA ENVIAR FECHA
        self.svCalendario.trace_add("write", self.enviarFecha)

    def enviarFecha(self, *args):
        self.svnacimiento.set('' + self.svCalendario.get())
        if len(self.calendar.get_date()) > 1:
            self.svCalendario.trace_add("write", self.calcularEdad)


        
    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%d/%m/%Y")

        self.result = self.fechaActual.year - self.conver.year
        self.result -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
        self.svedad.set(self.result)


        #BUSCADOR CONDICIONAL
    def buscarPacienteCondi(self):
        if len(self.svBuscadorCC.get()) > 0 or len(self.svBuscarApe.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscadorCC.get())) > 0:
                where = "WHERE documentoIdentidad = " + self.svBuscadorCC.get() + ""
            if (len(self.svBuscarApe.get())) > 0:
                where = "WHERE apellidoPaterno LIKE '" + self.svBuscarApe.get()+"%' AND activo=1"
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()


    def LimpiarBusqueda(self):
        self.svBuscadorCC.set("")
        self.svBuscarApe.set("")              
        self.tablaPaciente()


        #GUARDAR PACIENTES
    def guardarPaciente(self):
        persona = Persona(
            self.svnombre.get(), self.svapepater.get(), self.svapemater.get(), self.svdni.get(), self.svnacimiento.get(),
            self.svedad.get(), self.svantecedentes.get(), self.svcorreo.get(), self.svdireccion.get(), self.svtelefono.get()
        )

        if self.idPersona == None:
            guardarDatosPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)
        
        self.deshabilitar_campos()
        self.tablaPaciente()


    def habilitar_campos(self):
        #self.idPersona = None
        self.entrynombre.config(state="normal")
        self.entryapepater.config(state="normal")
        self.entryapemater.config(state="normal")
        self.entrydni.config(state="normal")
        self.entrynacimiento.config(state="normal")
        self.entryedad.config(state="normal")
        self.entryantecedentes.config(state="normal")
        self.entrycorreo.config(state="normal")
        self.entrydireccion.config(state="normal")
        self.entrytelefono.config(state="normal")

        self.btn_guardar.config(state="normal")
        self.btn_cancelar.config(state="normal")
        self.btncalendario.config(state="normal")

        self.svnombre.set("")
        self.svapepater.set("")
        self.svapemater.set("")
        self.svdni.set("")
        self.svnacimiento.set("")
        self.svedad.set("")
        self.svantecedentes.set("")
        self.svcorreo.set("")
        self.svdireccion.set("")
        self.svtelefono.set("")


    def deshabilitar_campos(self):
        self.idPersona = None
        self.svnombre.set("")
        self.svapepater.set("")
        self.svapemater.set("")
        self.svdni.set("")
        self.svnacimiento.set("")
        self.svedad.set("")
        self.svantecedentes.set("")
        self.svcorreo.set("")
        self.svdireccion.set("")
        self.svtelefono.set("")
        

        self.entrynombre.config(state="disabled")
        self.entryapepater.config(state="disabled")
        self.entryapemater.config(state="disabled")
        self.entrydni.config(state="disabled")
        self.entrynacimiento.config(state="disabled")
        self.entryedad.config(state="disabled")
        self.entryantecedentes.config(state="disabled")
        self.entrycorreo.config(state="disabled")
        self.entrydireccion.config(state="disabled")
        self.entrytelefono.config(state="disabled")


        self.btn_guardar.config(state="disabled")
        self.btn_cancelar.config(state="disabled")
        self.btncalendario.config(state="disabled")


    def tablaPaciente (self, where = ""):

        if len(where) > 0:
            self.listaPersona=listarCondicion(where)

        else:
            self.listaPersona=listar()


        self.tabla = ttk.Treeview(self, column=("Nombre", "1 Apellido", "2 Apellido", "DNI", "Nacimiento", "edad",
                                                "Antecedentes", "E-Mail", "Dirección", "Tel"))
        self.tabla.grid(row=11, column=0, columnspan=11, padx=10, pady=5, sticky="nse")
        
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=11, column=12, sticky="nse")

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure("evenrow", background="#ADC388")
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="NOMBRE")
        self.tabla.heading("#2", text="1 APELLIDO")
        self.tabla.heading("#3", text="2 APELLIDO")
        self.tabla.heading("#4", text="D. IDENTIDAD")
        self.tabla.heading("#5", text="FECHA NACIM")
        self.tabla.heading("#6", text="EDAD")
        self.tabla.heading("#7", text="ANTECEDENTES")
        self.tabla.heading("#8", text="E-MAIL")
        self.tabla.heading("#9", text="DIRECCIÓN")
        self.tabla.heading("#10", text="TELÉFONO")

        self.tabla.column("#0", anchor=W, width=60)
        self.tabla.column("#1", anchor=W, width=120)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=120)
        self.tabla.column("#4", anchor=W, width=100)
        self.tabla.column("#5", anchor=W, width=110)
        self.tabla.column("#6", anchor=W, width=60)
        self.tabla.column("#7", anchor=W, width=230)
        self.tabla.column("#8", anchor=W, width=130)
        self.tabla.column("#9", anchor=W, width=120)
        self.tabla.column("#10", anchor=W, width=100)


        for p in self.listaPersona:

            self.tabla.insert("",0,text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10]), tags=("evenrow",))

        self.btnEditarPaciente = tk.Button(self, text="EDITAR PACIENTE", command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20, bg="#000000", fg="#02FEEB", activebackground="#4A4B4D", font=("Mongolian Baiti", 12), cursor="hand2")
        self.btnEditarPaciente.grid(row=12, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text="ELIMINAR PACIENTE", command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20, bg="#000000", fg="#FF0013", activebackground="#304726", font=("Mongolian Baiti", 12), cursor="hand2")
        self.btnEliminarPaciente.grid(row=12, column=2, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text="HISTORIAL PACIENTE")
        self.btnHistorialPaciente.config(width=20, bg="#000000", fg="#FF00F0", activebackground="#304726", font=("Mongolian Baiti", 12), cursor="hand2")
        self.btnHistorialPaciente.grid(row=12, column=1, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text="SALIR", command=self.ventanaprincipal.destroy)
        self.btnSalir.config(width=15, bg="#611903", fg="#FFFFFF", activebackground="#B06853", font=("Mongolian Baiti", 12), cursor="hand2")
        self.btnSalir.grid(row=12, column=4, padx=10, pady=5)

    def editarPaciente (self):
        
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"] #TRAE EL ID
            self.nombre_paciente = self.tabla.item(self.tabla.selection())["values"][0]
            self.apepaterno_paciente = self.tabla.item(self.tabla.selection())["values"][1]
            self.apematerno_paciente = self.tabla.item(self.tabla.selection())["values"][2]
            self.dni_paciente = self.tabla.item(self.tabla.selection())["values"][3]
            self.nacimiento_paciente = self.tabla.item(self.tabla.selection())["values"][4]
            self.edad_paciente = self.tabla.item(self.tabla.selection())["values"][5]
            self.antecedentes_paciente = self.tabla.item(self.tabla.selection())["values"][6]
            self.email_paciente = self.tabla.item(self.tabla.selection())["values"][7]
            self.direccion_paciente = self.tabla.item(self.tabla.selection())["values"][8]
            self.tel_paciente = self.tabla.item(self.tabla.selection())["values"][9]

            self.habilitar_campos()

            self.entrynombre.insert(0, self.nombre_paciente)
            self.entryapepater.insert(0, self.apepaterno_paciente)
            self.entryapemater.insert(0, self.apematerno_paciente)
            self.entrydni.insert(0, self.dni_paciente)
            self.entrynacimiento.insert(0, self.nacimiento_paciente)
            self.entryedad.insert(0, self.edad_paciente)
            self.entryantecedentes.insert(0, self.antecedentes_paciente)
            self.entrycorreo.insert(0, self.email_paciente)
            self.entrydireccion.insert(0, self.direccion_paciente)
            self.entrytelefono.insert(0, self.tel_paciente)

        except:
            title = "EDITAR PACIENTE"
            mensaje = "Error al Editar, Inténtelo de Nuevo"
            messagebox.showerror(title, mensaje)

    
    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"]
            eliminarPaciente(self.idPersona)

            self.tablaPaciente()
            self.idPersona = None

        except:
            title = "ELIMINAR REGISTRO"
            mensaje = "No se completó la Eliminación"
            messagebox.showinfo(mensaje, title)

