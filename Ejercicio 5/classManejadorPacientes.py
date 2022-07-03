from classPaciente import Paciente
class ManejadorPacientes:
    
    i=0
    __pacientes=None
    def __init__(self):
        self.__pacientes=[]
    def agregarPaciente(self, paciente):
        paciente.rowid=ManejadorPacientes.i
        ManejadorPacientes.i+=1
        self.__pacientes.append(paciente)
    def getListaPacientes(self):
        return self.__pacientes
    def deletePaciente(self, paciente):
        i=self.obtenerIndicePaciente(paciente)
        self.__pacientes.pop(i)
    def updatePaciente(self, paciente):
        i=self.obtenerIndicePaciente(paciente)
        self.__pacientes[i]=paciente
    def obtenerIndicePaciente(self, paciente):
        bandera = False
        i=0
        while not bandera and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == paciente.rowid:
                bandera=True
            else:
                i+=1
        return i
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                pacientes=[paciente.toJSON() for paciente in self.__pacientes]
                )
        return d

