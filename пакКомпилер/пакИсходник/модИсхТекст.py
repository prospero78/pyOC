"""
Обеспечивает хранение исходного текста и его обработку.
"""

class тИсхТекст:
   def __init__(self, root, имя_файла):
      self.__исх = ""
      self.__имя_файла = имя_файла
      self.__Исх_Загрузить()
      
   def __Исх_Загрузить(self):
      try:
         файл = open(self.__имя_файла,'r', encoding='utf-8')
         self.__исх = файл.read()+" "*4
         файл.close()
      except FileNotFoundError:
         _текст = "Не могу открыть файл, файл="+self.__имя_файла
         self.ошибка.Печать( _текст)
         #файл.close()
   
   def Лит(self, поз):
      return self.__исх[поз]
   
   def __call__(self):
      return self.__исх
   
   @property
   def длина(self):
      return len(self.__исх)
