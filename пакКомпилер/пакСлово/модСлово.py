# coding: utf8
"""
Модуль предоставляет тип слова для построения AST.
Настройка пакета слов.
Слово -- кусочек текста в исходнике.
Обладает несколькими свойствами:
1. Литеры (само слово)
2. Координаты.
3. Строка, в которой он находится.
"""

from пакКомпилер.пакИсходник.модКоординаты import тКоорд

class тСлово:
	"""
		Тип тСлово описывает слово, как отдельную сущность в составе исходного
		текста, обладает различными атрибутами.
	"""
	кПусто, кМодуль, кМодульАлиас = range(3)
	def __init__(сам, пКорень, пКоорд, пстрСлово, пцНомерСлова):
		def Коорд_Проверить():
			бУсл = type(пКоорд) == тКоорд
			стрСообщ = "тСлово.__init__(): пКоорд должен быть тКоорд, type(пКоорд)="+str(type(пКоорд))
			пКорень.конс.Проверить(бУсл, стрСообщ)

		def Литеры_Проверить():
			бУсл = type(пстрСлово) == str
			стрСообщ = "тСлово.__init__(): пстрСлово должно быть строкой, type(пстрСлово)="+str(type(пстрСлово))
			пКорень.конс.Проверить(бУсл, стрСообщ)

			бУсл = len(пстрСлово) > 0
			стрСообщ = "тСлово.__init__(): пстрСлово не могут быть пустыми"
			пКорень.конс.Проверить(бУсл, стрСообщ)

		def НомерСлова_Проверить():
			бУсл = type(пцНомерСлова) == int
			стрСообщ = "тСлово.__init__(): пцНомерСлова должен быть целым, type(пцНомерСлова)="+str(type(пцНомерСлова))
			пКорень.конс.Проверить(бУсл, стрСообщ)

			бУсл = пцНомерСлова >= 0
			стрСообщ = "тСлово.__init__(): пцНомерСлова должен быть равен или больше 0, пцНомерСлова="+str(пцНомерСлова)
			пКорень.конс.Проверить(бУсл, стрСообщ)
			сам.__номер = пцНомерСлова

		сам.__корень = пКорень
		сам.конс = пКорень.конс

		Коорд_Проверить()
		Литеры_Проверить()
		НомерСлова_Проверить()

		сам.коорд = тКоорд(пКорень, пКоорд.стр, пКоорд.поз)
		сам.__стрСлово = пстрСлово
		сам.__слово_тип = тСлово.кПусто

	@property
	def слово(сам):
		return сам.__стрСлово

	@property
	def номер(сам):
		return сам.__номер

	def _Номер_Уст(сам, пцСлово):
		бУсл = type(пцСлово) == int
		стрОш = "тСлово.__init__(): пцСлово должен быть целым, type(пцСлово)="+str(type(пцСлово))
		сам.__корень.конс.Проверить(бУсл, стрОш)

		бУсл = пцСлово >= 0
		стрОш = "тСлово.__init__(): пцСлово должен быть равен или больше 0, пцСлово="+str(пцСлово)
		сам.__корень.конс.Проверить(бУсл, стрОш)

		сам.__номер = пцСлово

	def ЕслиИмя(сам):
		'''
		Проверяет на допустимость литер в слове для обнаружения имени сущности.
		'''
		# слово должно начинаться либо с "_", либо с буквы
		бВыход = False
		if сам.__стрСлово[0]=="_":
			бВыход = True
		elif сам.__стрСлово[0].isalpha():
			бВыход = True
		return бВыход

	def __str__(сам):
		стрСлово = сам.__стрСлово
		while len(стрСлово) < 7:
			стрСлово = " " + стрСлово
		return str(сам.__номер)+"\tслово="+ стрСлово + "\t" + str(сам.коорд)
