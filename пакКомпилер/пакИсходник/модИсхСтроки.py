"""
Модуль предоставляет тип для хранения строк исходника.
"""
class тИсхСтроки:
   def __init__(self, root, исх):
      self.__root = root
      self.__исх = исх
      self.__строки = {}
      self.__стр_всего=0
      self.__НаСтроки()
   
   def ПоСтр_Печать(self):
      счётчик1=1
      while счётчик1<self.__стр_всего:
         self.__root.конс.Исх_Печать(str(счётчик1) + " " + self.__строки[счётчик1])
         счётчик1 += 1
      
   def __НаСтроки(self):
      """
      Берёт исходный тест и разбивает на строки
      """
      лит=""
      строка = ""
      for лит in self.__исх:
         if лит!='\n':
            строка += лит
         else:
            self.__строки[self.__стр_всего+1]=строка
            self.__стр_всего += 1
            строка=""
   
   def __call__(self, номер):
      return self.__строки[номер]
      
   @property
   def всего(self):
      return len(self.__строки)
