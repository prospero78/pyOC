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
      self.app['time'] = "16:10"
      self.app['build'] = "Build"
      self.app['build_num'] = "054"
      
   def Язык_Уст(self, lang = "ru"):
      if True:
         self.app['name'] = 'Oberon-07 Compiler'
         self.winMain['log'] = 'Log'
         self.winMain['mnuFile'] = 'File'
         self.winMain['mnuExit'] = 'Exit'
         self.winMain['mnuOpen'] = 'Open...'
         
      if lang == "ru":
         self.Компиляция = "Компиляция"
         self.app['name'] = 'Компилятор Oberon-07'
         self.app['name1'] = 'Oberon-07'
         self.app['build'] = "Cборка"
         self.winMain['log'] = 'Лог'
         self.winMain['mnuFile'] = 'Файл'
         self.winMain['mnuExit'] = 'Выход'
         self.winMain['mnuOpen'] = 'Отрыть...'
