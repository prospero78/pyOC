# coding: utf8
"""
Модуль предоставляет класс для разбора типа.
Простой тип может содержать определения других подтипов и членов.
"""

from пакКомпилер.пакСлово import тСлово

class тТип:
   цУказатель = 1
   цМассив    = 2
   цЗапись    = 3
   def __init__(сам, пКорень):
      сам.__корень = пКорень
      сам.__имя = "" # имя типа
      сам.__род = 0 # Род типа -- POINTER TO, ARRAY, RECORD
      сам.__предок = "" # имя предка
      сам.__бЭкспорт = "" # признак экспорта
      сам.__слова = {} # Список слов типа

   @property
   def имя(сам):
      return сам.__имя

   @property
   def предок(сам):
      return сам.__предок

   @property
   def бЭкспорт(сам):
      return сам.__бЭкспорт

   def Эксп_Уст(сам, пбЭкспорт):
      бУсл = type(пбЭкспорт) == bool
      стрОш = "Признак экспорта типа может быть только BOOLEAN, type="+str(type(пбЭкспорт))
      сам.__корень.конс.Контроль(бУсл, стрОш)

      сам.__бЭкспорт = пбЭкспорт

   @property
   def слова(сам):
      return сам.__слова

   def Слово_Доб(сам, пСлово):
      бУсл = type(пСлово) == тСлово
      стрОш = "В слова типа можно добавить только тСлово, type="+str(type(пСлово))
      сам.__корень.конс.Контроль(бУсл, стрОш)

      сам.__слова[len(сам.__слова)] = пСлово
