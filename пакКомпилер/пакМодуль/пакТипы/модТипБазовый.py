# coding:utf8
"""
Содержит базовый тип для всех родов записей
"""

if True:
	from пакКомпилер.пакСлово import тСлово
	from пакКомпилер.пакМодуль.пакТипы.модРод import тРод

class тТипБазовый:
	def __init__(сам, пКорень, пСловаСекции):
		assert пКорень != None, "Корень компилятора не может быть None"
		сам.__корень = пКорень
		сам.ошибка = пКорень.ошибка
		сам.консоль = пКорень.конс

		сам.__бЭкспорт = False # признак экспорта
		сам.__стрИмя = ""

		сам.__предок = "" # предок текущего типа

		сам.__Имя_Получить()
		сам.__Экспорт_Проверить()
		сам.__Определитель_Проверить()
		сам.__Род_Проверить()

	def Ошибка_Печать(сам, пСлово, пСообщ):
		строка_исх = сам.__корень.исх.строки(пСлово.коорд.стр)
		сам.консоль.Печать(сам.__корень.исх.строки(пСлово.коорд.стр))
		сам.ошибка.Коорд(пСообщ, пСлово.коорд, пСлово.строка)

	def __Род_Проверить(сам):
		"""
		Устанавливает род типа:
		1. Алиас встроенного типа
		2. Массив
		3. Запись
		4. Указатель
		5. Процедура
		Обрезать слова секции нельзя. Иначе потом не узнаем
		какой тип алиаса используется.
		"""
		тип_встроен = ["BOOLEAN", "CHAR", "INTEGER", "REAL", "BYTE", "SET"]
		строка_род = сам.Слово_Проверить()
		if строка_род in тип_встроен:
			сам.__род = тРод.сВстроен
		elif строка_род == "ARRAY":
			сам.__род = тРод.сМассив
		elif строка_род == "RECORD":
			сам.__род = тРод.сЗапись
		elif строка_род == "POINTER":
			сам.__род = тРод.сУказатель
		elif строка_род == "PROCEDURE":
			сам.__род = тРод.сПроцедура
		else:
			assert False, "тТипБазовый: Неизвестный род типа, род="+строка_род

	@property
	def предок(сам):
		return сам.__предок

	def Двоеточие_Обрезать(сам):
		"""
		Здесь может быть как ":", так и "=".
		Первый для описания конечного поля,
		второй для описания встроенной записи.
		"""
		бВыход = False
		строка_двоеточ = сам.Слово_Проверить()
		if строка_двоеточ == ":": # есть двоеточие
			сам.СловаСекции_Обрезать()
			бВыход = True
		elif строка_двоеточ == "=": # есть внутренняя запись
			pass
		else: # а это уже непонятно что
			assert строка_двоеточ != тСлово, "тТипБазовый: строка должна быть ':' или '=',    строка=" + строка_двоеточ
		return бВыход

	@property
	def корень(сам):
		return сам.__корень
