"""
Предоставляет класс графики для компилятора Оберона.
"""

from .пакОкнГлав import тОкнГлав

class тГуи:
   def __init__(self, root)->None:
      self.окнГлав = тОкнГлав(root)

   def Пуск(self)->None:
      self.окнГлав.Пуск()
