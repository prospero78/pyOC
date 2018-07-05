# coding: utf8
"""
Модуль "Компилер".
Содержит в себе все составляющие для компилятора Оберона
"""
if True:
	from .пакДиагностика.модКонсоль import тКонсоль
	from .пакДиагностика import тОшибка
	from .пакИсходник import тИсходник
	from .пакРесурс import тРесурс
	from .пакГуи import тГуи

class тКомпилер:
	def __init__(self):
		self.рес = тРесурс(self)
		self.конс = тКонсоль(self)
		self.ошибка = тОшибка(self)
		self.исх = тИсходник(self, "Hello.o7")
		self.гуи = тГуи(self)


	def Пуск(self):
		self.конс.Печать(self.рес.Компиляция)
		self.исх.Обработать()
		self.гуи.Пуск()
