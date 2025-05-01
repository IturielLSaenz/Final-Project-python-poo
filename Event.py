#--- Clase Event: ------------
# Autor: Ituriel Liebes Sáenz
# ID: 554644
# Semestre: 3er Semestre.
#------------------------------
import Person as P
import Date as D
import Time as T

class Event:
    def __init__(self,subject:str,desc:str,person=P.Person("N/A","N/A","N/A"),fecha=D.Date(2000,1,1),horaDeInicio=T.Time(00,00,00),horaDeFinalizacion=T.Time(00,00,00)):
        self.__subject=subject
        self.__desc=desc
        self.__person=person
        self.__fecha=fecha
        self.__hrInicio=horaDeInicio
        self.__hrFin=horaDeFinalizacion
    @property
    def subject(self) -> str:
        return self.__subject
    @subject.setter
    def subject(self,subject:str):
        self.__subject=subject
    @property
    def desc(self) -> str:
        return self.__desc
    @desc.setter
    def desc(self,desc:str):
        self.__desc=desc
    def previewToString(self): # regresa un string corto para una preview de los datos del evento!
        return f"Asunto: {self.__subject} | Fecha: {self.__fecha.toString()}"
    #metodo toString completo:
    def toString(self):
        return f"Asunto: {self.__subject} \nFecha: {self.__fecha.toString()} \nHora de inicio: {self.__hrInicio.toString()} \nHora de finalización: {self.__hrFin.toString()} \nDescripción: {self.__desc}"