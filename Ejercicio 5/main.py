from classPaciente import Paciente
from classManejadorPacientes import ManejadorPacientes
from classObjectEncoder import ObjectEncoder
from classRepositorioPacientesJSON import RespositorioPacientes
from vistaPacientes import PacienteList, PacientsView
from classControladorPacientes import ControladorPacientes
   
if __name__=='__main__':

    json = ObjectEncoder('C:/Users/herna/Documents/POO/pipup/Ejercicio 5/pacientes.json')
    manejador=ManejadorPacientes()
    diccionario=json.leerJSONArchivo()
    manejador=json.decodificarDiccionario(diccionario)
    repo=RespositorioPacientes(json)
    vista=PacientsView()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()


