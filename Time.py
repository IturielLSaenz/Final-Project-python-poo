#Ejercicio 3: Clase Hora
#Ituriel Liebes Sáenz

class Time:
    #constructor
    def __init__(self, hour=00, minute=00, second=00):
        if(hour>=0 & hour<24):
            self.__hour = hour
        else:
            print("No es un valor adecuado para la hora!")
        #
        if(minute>=0 & minute <59):
            self.__minute = minute
        else:
            print("No es un valor adecuado para los minutos!")
        if(second>=0 & second<59):
            self.__second = second
        else:
            print("No es un valor adecuado para los segundos!")
    #metodos:
    #getter
    @property
    def hour(self):
        return self.__hour
    @property
    def minute(self):
        return self.__minute
    @property
    def second(self):
        return self.__second
    #setter
    @hour.setter
    def hour(self, hour):
        self.__hour = hour
    @minute.setter
    def minute(self, minute):
        self.__minute = minute
    @second.setter
    def second(self, second):
        self.__second = second
    #otros metodos
    def incrementHour(self, increment):
        if self.__hour+increment>=24:
            self.__hour=00
            self.__hour+=(increment-1)
    def incrementMinute(self, increment):
        if self.__minute+increment>=60:
            self.__minute=00
            self.__minute+=(increment-1)
            if self.__hour+increment>=24:
                self.__hour=00
                self.__hour+=(increment-1)
    def incrementSecond(self, increment):
        #incrementar reloj por segundos
        if self.__second+increment>=60:
            #regresamos a cero:
            self.__second=00
            #le sumamos el incremento menos 1
            #ya que se utilizó para aumentar los
            #minutos
            self.__second+=(increment-1)
            self.__minute+=1
            if self.__minute==60:
                self.__minute=00
                self.hour+=1
    def toString(self):
        return (str(self.__hour).zfill(2)+":"+str(self.__minute).zfill(2)+":"+str(self.__second).zfill(2))