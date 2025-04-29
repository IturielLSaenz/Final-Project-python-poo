#Archivo de la clase Date para representar una fecha
 


class Date:
    #Método constructor (con valores por omisión)
    def __init__(self, year=2000, month=1, day=1):
        self.Year = year
        self.Month = month
        self.Day = day 
    
    #Método que requiero para checar si el año es bisiesto o no
    def leapYear(self):
        return self.__year%4==0 and (self.__year%100!=0 or self.__year%400==0)
    
    @property 
    def Year(self):
        return self.__year
    @property 
    def Month(self):
        return self.__month 
    @property 
    def Day(self):
        return self.__day 
    @Year.setter 
    def Year(self, year):
        if(year>0):
            self.__year = year
        else:
            self.__year = 2000
    @Month.setter 
    def Month(self, month):
        if(month>0  and month<13):
            self.__month = month 
        else: 
            self.__month = 1
    @Day.setter
    def Day(self, day):
        if(self.__month in [1, 3, 5, 7, 8, 10, 12]):
            limiteSuperior = 31
            #o los meses de 30 días
        elif(self.__month in [4, 6, 9, 11]):
            limiteSuperior = 30
            #o si es febrero, checamos si es año bisiesto o no
        elif(self.leapYear()):
            limiteSuperior = 29
        else:
            limiteSuperior = 28
        if(day>0 and day<=limiteSuperior):
            self.__day = day 
        else: 
            self.__day = 1
    
    #método para poner en formato de texto
    def toString(self):
        if(self.__day<10):
            d = "0" + str(self.__day)
        else:
            d= str(self.__day)
        if(self.__month<10):
            m = "0" + str(self.__month)
        else:
            m = str(self.__month)
        if(self.__year<10):
            y = "000" + str(self.__year)
        elif(self.__year<100):
            y = "00" + str(self.__year)
        elif(self.__year<1000):
            y = "0" + str(self.__year)
        else:
            y = str(self.__year)
        return d + "/" + m + "/" + y
    
    #Métodos para incrementar
    def incYear(self):
        self.__year = self.__year + 1
    def incMonth(self):
        self.__month = self.__month + 1
        if(self.__month > 12):
            self.__month=1
            self.incYear()
    def incDay(self):
        self.__day = self.__day + 1
        if(self.__month in [1, 3, 5, 7, 8, 10, 12]):
            maxNumDays = 31
            #o los meses de 30 días
        elif(self.__month in [4, 6, 9, 11]):
            maxNumDays = 30
            #o si es febrero, checamos si es año bisiesto o no
        elif(self.leapYear()):
            maxNumDays = 29
        else:
            maxNumDays = 28
        if(self.__day > maxNumDays):
            self.__day = 1
            self.incMonth()
    #Decrementos
    def decYear(self):
        self.__year = self.__year - 1
        if(self.__year<0):
            print("Se alcanzó el año cero. No se puede decrementar más.")
            self.__year = 0
    def decMonth(self):
        self.__month = self.__month - 1
        if(self.__month < 1):
            self.__month=12
            self.decYear()
    def decDay(self):
        self.__day = self.__day - 1
        m = self.__month-1 
        if(m<1):
            m = 12
        if(m in [1, 3, 5, 7, 8, 10, 12]):
            maxNumDaysPreviousMonth = 31
            #o los meses de 30 días
        elif(m in [4, 6, 9, 11]):
            maxNumDaysPreviousMonth = 30
            #o si es febrero, checamos si es año bisiesto o no
        elif(self.leapYear()):
            maxNumDaysPreviousMonth = 29
        else:
            maxNumDaysPreviousMonth = 28
        if(self.__day < 1):
            self.__day = maxNumDaysPreviousMonth
            self.decMonth()
    