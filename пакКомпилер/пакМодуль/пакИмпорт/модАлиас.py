"""
Модуль предоставляет тип для хранения имени модуля и его алиаса.
"""

class тАлиас:
   def __init__(self, алиас, имя, номер):
      assert type(алиас) == str, "Алиас должен быть строкой, type="+type(алиас)
      self.__алиас = алиас

      assert type(имя) == str, "Имя должно быть строкой, type="+type(имя)
      assert имя != "", "Имя не может быть пустым"
      self.__имя = имя

      assert type(номер) == int, "Номер должно быть целым, type="+type(номер)
      self.__номер = номер

   @property
   def алиас(self):
      return self.__алиас

   @property
   def имя(self):
      return self.__имя

   @property
   def бАлиас(self):
      if self.__алиас == "":
         бАлиас = False
      else:
         бАлиас = True
      return бАлиас

   @property
   def номер(self):
      return self.__номер
