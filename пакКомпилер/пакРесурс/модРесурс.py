"""
Содержит класс ресурсов.
"""

class тРесурс:
   def __init__(self, root):
      self.__root = root
      self.app = {}
      self.winMain = {}
      self.Шапка()
      self.Язык_Уст()
   
   def Шапка(self):
      self.app['date'] = "2018-02-26"
      self.app['time'] = "15:21"
      self.app['build'] = "Build"
      self.app['build_num'] = "053  "

   def Язык_Уст(self, lang = "ru"):
      if True:
         self.app['name'] = 'Oberon-07 Compiler'
         self.winMain['log'] = 'Log'
      if lang == "ru":
         self.Компиляция = "Компиляция"
         self.app['name'] = 'Компилятор Oberon-07'
         self.app['name1'] = 'Oberon-07'
         self.app['build'] = "Cборка"
         self.winMain['log'] = 'Лог'
