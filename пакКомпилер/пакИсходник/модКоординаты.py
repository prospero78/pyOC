"""
Модуль предоставляет тип координат тега в исходном тексте.
Координаты не меняются.
"""
class тКоорд:
   def __init__(self, стр, поз):
      assert type(стр) == int, "тКоорд.__init__(): стр должен быть числом, type(стр)="+str(type(стр))
      assert стр >= 0, "тКоорд.__init__(): стр должен быть 0 или больше, стр="+str(стр)
      self.__стр=стр
      
      assert type(поз) == int, "тКоорд.__init__(): поз должен быть числом, type(поз)="+str(type(поз))
      assert поз >= 0, "тКоорд.__init__(): поз должен быть 0 или больше, поз="+str(поз)
      self.__поз=поз
   
   @property
   def стр(self):
      return self.__стр
   
   @property
   def поз(self):
      return self.__поз
   
   def __str__(self):
      return "Коорд: стр="+str(self.__стр)+"   поз="+str(self.__поз)
