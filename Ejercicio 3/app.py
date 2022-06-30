from tkinter import *
from tkinter import ttk, messagebox
from API import Dolar

class Aplicacion:
    __datos = None
    __dolares= None
    __ventana = None
    __precioDolar = None
    
    
    def __init__(self):
        api = Dolar()
        api.Run()
        
        self.__precioDolar= api.getResultado()
        self.__ventana = Tk()
        self.__ventana.geometry('250x240')
        self.__ventana.title('API -  Precio del Dolar 💰')
        mainframe = ttk.Frame(self.__ventana, padding = '3 3 12 12')
        
        mainframe.grid(column= 0, row = 0)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        
        mainframe = Frame(self.__ventana)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__pesos = StringVar()
        self.__dolares = StringVar()
        self.__dolares.trace('w', self.calcular)
        self.dolaresEntry = Entry(mainframe, width=7, textvariable=self.__dolares)
        self.dolaresEntry.grid(column=2, row=1, sticky=(W, E))
        Label(mainframe, textvariable=self.__pesos).grid(column=2, row=2, sticky=(W, E))
        Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        Label(mainframe, text="dolares").grid(column=3, row=1, sticky=W)
        Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        Label(mainframe, text="pesos").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            self.dolaresEntry.focus()
            self.__ventana.mainloop()
    def calcular(self, *args):
        if self.dolaresEntry.get()!='':
            try:
                valor=float(self.dolaresEntry.get())
                precio=float(str(self.__preciodolar[0]['casa']['venta']).replace(",","."))
                self.__pesos.set(valor*precio)
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
                self.__dolares.set('')
                self.dolaresEntry.focus()
        else:
            self.__pesos.set('')
        
        
        
        
        
        self.__ventana.mainloop()
    
    
    
    