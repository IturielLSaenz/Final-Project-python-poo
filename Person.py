#--- Clase Person: ------------
# Autor: Ituriel Liebes Sáenz
# ID: 554644
# Semestre: 3er Semestre.
#------------------------------
class Person:
    def __init__(self,name="N/A",tel="N/A",email="N/A"): #definir tel como str!
        self.__name=name
        self.__tel=tel
        self.__email=email
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self,name:str):
        self.__name=name
    @property
    def tel(self) -> str:
        return self.__tel
    @tel.setter
    def tel(self,tel:str):
        if(len(tel)==10):
            self.__tel=tel
        else:
            print("El numero de teléfono es inválido! (10 caracteres!)")
            self.__tel="N/A"
    @property
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self,email:str):
        self.__email=email
    def toString(self):
        return f"Name: {self.__name} ; Tel: {self.__tel} ; Email: {self.__email}"