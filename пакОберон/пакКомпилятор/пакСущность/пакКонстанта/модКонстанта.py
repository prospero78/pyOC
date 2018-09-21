# coding: utf8
"""
Модуль описывает сущность константы.
У неё несколько полей:
1. Имя
2. Модуль
3. Тип
4. Значение
5. Ссылка ни исх строку
6. Координаты в исходной строке
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакКоорд import тКоордФикс
	from пакОберон.пакКомпилятор.пакСущность.пакОшибка import тОшибка

class тКонстанта:
	def __init__(сам, пОберон, пДанные):
		сам.__оберон = пОберон
		сам.__конс = пОберон.конс
		сам.__конс.Отладить("тКонстанта.__init__()")

		сам.ош = тОшибка(пОберон, "тКонстанта")

		сам.__слово = пДанные['слово'] # Ссылка на исходную строку
		сам.__имя = сам.__слово.строка
		сам.__бЭкспорт = пДанные['бЭкспорт']
		сам.__модуль_имя = пДанные['модуль_имя']
		сам.__тип = "" # У констант изначально тип неизвестен
		сам.__знач = "" # Первоначальное значение неизвестно, хранится в виде строки.

	def Выраж_Вычислить(сам):
		"""
		Охренительная задача по вычислению выражения у константы.
		На этапе разбора все константы неизвестны, поэтому этот метод
		вызывается при рассмотрении выражений.
		1. Сначала надо вычислить род встреченного слова. Это могут быть:
			числа
			строки
			булевы значения и т. д.
		"""

	@property
	def имя(сам) -> str:
		if сам.__имя == "":
			сам.ош.Внутр("имя", "Имя константе не присвоено!")
			return ""
		return сам.__имя

	@property
	def модуль(сам)-> str:
		if сам.__модуль_имя == "":
			сам.ош.Внутр("модуль", "Имя модулю не присвоено!")
			return ""
		return сам.__модуль_имя

	@property
	def тип(сам) -> str:
		if сам.__тип == "":
			сам.ош.Внутр("тип", "Тип константе не присвоен!")
			return ""
		return сам.__тип

	@property
	def знач(сам) -> str:
		if сам.__знач == "":
			сам.ош.Внутр("знач", "Значение константе не присвоено!")
			return ""
		return сам.__знач

	@property
	def слово(сам) -> тСлово:
		return сам.__слово

	@property
	def коорд(сам) -> тКоордФикс:
		return сам.__слово.коорд
