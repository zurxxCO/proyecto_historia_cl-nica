import tkinter as tk
from PACIENTE.gui import Frame

def main():
    ventanaprincipal=tk.Tk()
    ventanaprincipal.title("ARCHIVO DE HISTORIAS MÉDICAS")
    ventanaprincipal.resizable(0,0)

    app = Frame(ventanaprincipal)

    app.mainloop()


if __name__ == "__main__":
    main()
