"""
Модуль предоставляет класс для разбора типа.
"""

from пакКомпилер.пакТег.модТег import тТег

class тТип:
   def __init__(self, root):
      self.__root = root
      self.__имя = "" # имя типа
      self.__предок = "" # имя предка
      self.__бЭкспорт = "" # признак экспорта
      self.__теги = {} # Список тегов типа
   
   @property
   def имя(self):
      return self.__имя
   
   @property
   def предок(self):
      return self.__предок
   
   @property
   def бЭкспорт(self):
      return self.__бЭкспорт
   
   def Эксп_Уст(self, эксп):
      усл = type(эксп) == bool
      _текст = "Признак экспорта типа может быть только BOOLEAN, type="+str(type(эксп))
      self.__root.конс.Контроль(усл, _текст)
      self.__бЭкспорт = эксп
   
   @property
   def теги(self):
      return self.__теги
   
   def Тег_Доб(self, тег):
      усл = type(тег) == тТег
      _текст = "В теги типа можно добавить только тТег, type="+str(type(тег))
      self.__root.конс.Контроль(усл, _текст)
      self.__теги[len(self.__теги)] = тег
