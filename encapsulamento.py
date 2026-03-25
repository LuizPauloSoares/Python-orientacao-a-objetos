class controleTemperatura:
    def __init__(self, temperatura):
          self.__temperatura = temperatura

    @property
    def temperatura(self):
         return self.__temperatura
    
    @temperatura.setter
    def temperatura(self,temperatura):
         if temperatura < -50 or temperatura > 100:
              print("temperatura invalida ")     
         else:
              self.__temperatura =  temperatura

    def converter_para_fahrenheit(self):
        return  (self.temperatura*1.8)+32

def main():  
    temp = controleTemperatura(0)
    print(temp.temperatura)  

    sc = int(input("me informa a temperatura : "))
    temp.temperatura = sc 
    print(temp.temperatura)

    print(temp.converter_para_fahrenheit())

if __name__ == "__main__":
    main()
