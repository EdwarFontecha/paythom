class Bebida:
    def __init__(self,nombre):
        self.__nombre = nombre
        
    def getObtenerNombre(self):
      return f"La bebida es {self.__nombre}"
  
class Cerveza(Bebida):
    def __init__(self, nombre , marca, alcohol):
      super().__init__(nombre)
      self.__marca = marca
      self.__alcohol = alcohol
      
    def getObtenerNombre(self):
        return f"{super().getObtenerNombre()} de la marca{self.__marca} con grados de alcohol{self.__alcohol}"
    
Cerveza = Cerveza("poker","Bavaria", 4.0)
print(Cerveza.getObtenerNombre())
        
