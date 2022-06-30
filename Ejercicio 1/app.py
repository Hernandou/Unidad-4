from tkinter import *
from tkinter import ttk, messagebox
from turtle import width

from sqlalchemy import column

class Aplicacion:
    
    __ventana = None
    __peso = None
    __metros = None
    __IMC = None
    __condic = ''

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('400x250')
        self.__ventana.title('Calculadora facherita de IMC 💪🏻')

        mainframe = ttk.Frame(self.__ventana, padding = '3 3 12 12')
        mainframe.grid(column= 0, row = 0, sticky= (N,W,E,S))
        mainframe.columnconfigure(0,  weight= 1)
        mainframe.rowconfigure(0, weight= 1)
        
        self.__peso = StringVar()
        self.__metros = StringVar()
        self.__IMC = StringVar()
        self.__condic = StringVar()
        self.pesoEntry = ttk.Entry(mainframe, width = 10, textvariable= self.__peso)
        self.pesoEntry.grid(column = 2,row = 1, sticky=(S,E)) 
                
        ttk.Label(mainframe,text = '   Ingrese su PESO 😈 [KG]: ').grid(column=1, row = 1, sticky = E)
        self.metrosEntry = ttk.Entry(mainframe, width = 10, textvariable= self.__metros)
        self.metrosEntry.grid(column = 2,row = 2, sticky = E)
        ttk.Label(mainframe, text= '     Ingrese su ALTURA 😈 [CM]: ').grid(column=  1,row= 2)
        ttk.Label(mainframe, textvariable = self.__IMC).grid(column= 2, row = 3)
        ttk.Label(mainframe, textvariable= self.__condic).grid(column = 2, row = 4)

        ttk.Button(mainframe, text = 'Calcular', command= self.calcular).grid(column = 2, row = 5)
        ttk.Label(mainframe, text = 'El IMC es:  ').grid(column= 1,row= 3)
        ttk.Button(mainframe, text = 'Salir', command = self.__ventana.destroy).grid(column= 1, row = 5)
        ttk.Label(mainframe, text = 'Estado del Paciente: ').grid(column=1,row = 4)
        self.__ventana.mainloop()
    

    
    def calcular(self):
        
        try:
            peso = float(self.pesoEntry.get())
            estatura = float(self.metrosEntry.get())
            val = peso / ((estatura)/100) ** 2
            round(val)
            self.__IMC.set(val)
            
            if(val  < 18.5):
                condic = 'Peso inferior al normal'
                self.__condic.set(condic)
                
            elif(val >= 18.5 or val<= 24.9 ):
                condic = 'Peso Normal'
                self.__condic.set(condic)
                
            elif(val > 30.0):
                condic = 'Persona con sobrepeso'
                self.__condic.set(condic)

            
            self.__IMC.set(val)
            
            
        except ValueError:
            messagebox.showerror(title = 'Error', message = 'Error de tipo de valor.')
            