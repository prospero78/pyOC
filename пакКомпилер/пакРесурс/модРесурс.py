"""
Содержит класс ресурсов.
"""

class тРесурс:
   def __init__(self, root):
      self.__root = root
      self.app = {}
      self.app['name'] = 'Oberon-07 Compiler'
      self.Шапка()
      self.Язык_Уст()
   
   def Шапка(self):
      self.app['date'] = "2018-02-26"
      self.app['time'] = "12:41"
      self.app['build'] = "049"

   def Язык_Уст(self, lang = "ru"):
      if lang == "ru":
         self.Компиляция = "Компиляция"
         self.app['name'] = 'Компилятор Oberon-07'
