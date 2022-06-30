from tkinter import *
from tkinter import ttk, messagebox


class Aplicacion:

    __ventana = None
    __precioBase = None
    __IVA = None
    __txt = None
    __total = None

    def __init__(self):

        self.__ventana = Tk()
        self.__ventana.geometry('450x350')
        self.__ventana.title('Calculadora IVA 🤑 💶')

        mainframe = ttk.Frame(self.__ventana, padding='3 3 12 12')
        mainframe.grid(column=0, row=0)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        # Variables
        self.__precioBase = StringVar()
        self.__txt = StringVar()
        self.__IVA = StringVar()
        self.__total = StringVar()

        # Barras de Entrada
        self.precioEntry = ttk.Entry(mainframe, width=10, textvariable=self.__precioBase).grid(column=2, row=3)

        # Barras de Texto
        ttk.Label(mainframe, text='Ingrese Precio Base ').grid(column=1, row=3)
        ttk.Label(mainframe, text='El IVA es: ').grid(column=1, row=4)
        ttk.Label(mainframe, text = 'Precio TOTAL: ').grid(column = 1,row= 5)
        ttk.Label(mainframe, textvariable=self.__txt).grid(column=2, row=4)
        ttk.Label(mainframe, textvariable = self.__total). grid(column = 2, row =5)
        # Check Boxes
        Radiobutton(mainframe, text='IVA 21%', variable=self.__IVA, value='21').grid(column=1, row=7)
        Radiobutton(mainframe, text='IVA 10.5%', variable=self.__IVA, value='10.5').grid(column=2, row=7)

        # Botones
        ttk.Button(mainframe, text='Calcular', command=self.calcular).grid(column=2, row=10)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=1, row=10)

        self.__ventana.mainloop()

    def calcular(self):

        if(self.__IVA.get() == '21'):
        
            iva = (float(self.__precioBase.get())*21)/100
            total = (float(self.__precioBase.get())) + iva
            self.__txt.set(iva)
            self.__total.set(total)
            print(self.__txt)

        elif(self.__IVA.get() == '10.5'):
            iva = (float(self.__precioBase.get()) * 10.5) / 100
            total = (float(self.__precioBase.get())) + iva
            self.__txt.set(iva)
            self.__total.set(total)
