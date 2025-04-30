#--- Clase Agenda: ------------
# Autor: Ituriel Liebes Sáenz
# ID: 554644
# Semestre: 3er Semestre.
#------------------------------
import Person as P
import Event as E

class Agenda():
    def __init__(self):
        self.__owner="User"
        self.__events = []
    def __init__(self,owner=P.Person()):
        self.__owner=owner
        self.__events = [] #lista inicial de eventos
    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, person:P.Person):
        self.__owner = person
    @property
    def events(self):
        return self.__events
    @events.setter
    def events(self):
        self.__events = []
    #otros metodos
    def addEvent(self, newEvent):
        self.__events.append(newEvent) #mete el nuevo evento en la lista
    def removeEvent(self, index): #<- actualizar esto!!!!!!
        self.__events.pop(index) #el argumento pop recibe un index y elimina el elemento en dicha posición
    # def show(self): <- queda pendiente este metodo!!!
    #     for i in self.__events:
    #         print(i) 
    def getEventsList(self):
        result = [] #lista completa
        for index in range(len(self.__events)):
            result.append(f"Evento {index + 1}: {self.__events[index].toString()}")
        return "\n".join(result)
    def getEventAtIndex(self, index):
        return (self.__events[index])
