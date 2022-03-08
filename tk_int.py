from tkinter import Label, messagebox
from tkinter.constants import CENTER
from tkinter import *
from tkinter import ttk
from functions import Funciones


class Ventanita():
    """"
    La clase de ventanita afsafsafsafsafa
    """
    def __init__(self, window):
        self.objeto_base = Funciones()
        self.root = window
        window.geometry('500x500')
        window.title('UNIVERSIDAD DE BUENOS AIRES')
        # Labels
        self.label1 = Label(window, text='Ingrese sus datos: ', font=(12))
        self.label1.pack(anchor=CENTER)
        self.label1.config(bg='lightgreen', width=400)

        self.l_nombre = Label(window, text="Nombre",
                              font=(10)).place(x=0, y=45)

        self.l_apellido = Label(
            self.root, text="Apellido", font=(10)).place(x=0, y=90)

        self.l_DNI = Label(window, text="DNI",
                           font=(10)).place(x=0, y=135)

        self.l_id = Label(window, text="ID",
                          font=(10)).place(x=250, y=45)

        # Botones

        self.boton_alta = Button(self.root, text="Alta", command=self.alta_tk, padx=10,
                                 pady=3, activebackground="green", activeforeground="white")
        self.boton_alta.place(x=40, y=200)
        self.boton_baja = Button(window, text="Borrar registro",
                                 command=self.baja_tk, padx=10, pady=3)
        self.boton_baja.place(x=305, y=70)
        self.actualizar_tree = Button(self.root, text="Actualizar lista", command=self.tk_tree, padx=10,
                                      pady=3, activebackground="green", activeforeground="white")
        self.actualizar_tree.place(x=175, y=200)
        boton_modificar = Button(self.root, text="Modificar",
                                 command=self.modif_tk, padx=10, pady=3)
        boton_modificar.place(x=350, y=200)

        # Entrys

        self.nombre = Entry(window)
        self.apellido = Entry(window)
        self.dni = Entry(window)
        self.id = Entry(window)

        self.nombre.place(x=100, y=45)
        self.apellido.place(x=100, y=90)
        self.dni.place(x=100, y=135)
        self.id.place(x=300, y=45)

        # Tree
        self.tree = ttk.Treeview(window)
        self.tree['columns'] = ('col1', 'col2', 'col3')
        self.tree.column("#0", width=80, minwidth=80, anchor=W)
        self.tree.column("col1", width=110, minwidth=110)
        self.tree.column("col2", width=110, minwidth=110)
        self.tree.column("col3", width=130, minwidth=130)

        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Nombre")
        self.tree.heading("#2", text="Apellido")
        self.tree.heading("#3", text="DNI")

        self.tree.place(x=40, y=250)

    def alta_tk(self):
        """
        Hola hola hola
        """
        datos = (self.nombre.get(), self.apellido.get(), self.dni.get())
        self.objeto_base.alta(datos)
        messagebox.showinfo(
            'Ventana', 'La base de datos ha sido actualizada')

    def baja_tk(self):
        id = (self.id.get())
        self.objeto_base.baja(id)
        messagebox.showinfo(
            'Ventana', 'El registro ha sido eliminado')

    def modif_tk(self):
        nombre = (self.nombre.get())
        apellido = (self.apellido.get())
        dni = (self.dni.get())
        aid = (self.id.get())

        self.objeto_base.modificar(nombre, apellido, dni, aid)
        messagebox.showinfo(
            'Ventana', 'El registro ha sido modificado')

    def tk_tree(self):
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)
        cur = self.objeto_base.actualizar_tree(
            "SELECT id,nombre, apellido, dni FROM trabajo_final")
        print(self.nombre, self.apellido, self.dni)
        self.tree.insert('', 0, text=self.nombre, values=self.apellido)
