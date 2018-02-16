"""
Содержит класс ресурсов.
"""

class тРесурс:
   def __init__(self, root):
      self.__root = root
      self.Шапка()
      self.Язык_Уст()
   
   def Шапка(self):
      self.дата = "2018-02-16"
      self.время = "11:12"
      self.сборка = "043"

   def Язык_Уст(self, lang = "ru"):
      if lang == "ru":
         self.Компиляция = "Компиляция"
