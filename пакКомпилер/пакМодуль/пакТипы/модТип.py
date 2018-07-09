# coding: utf8
"""
Модуль предоставляет класс для разбора типа.
Простой тип может содержать определения других подтипов и членов.
"""

if True:
	from пакКомпилер.пакСлово import тСлово

class тТип:
	цУказатель = 1
	цМассив    = 2
	цЗапись    = 3
	def __init__(сам, пКорень, пСловаСекции):
		
		assert пКорень != None, "тТип: Корневая привязка не может быть None"
		сам.__корень = пКорень
		
		assert len(пСловаСекции) > 1, "тТип: Неполное определение секции"
		сам.__слова_секции = пСловаСекции # Список слов типа

		стрИмя = пСловаСекции[0]
		assert стрИмя != тСлово, "тТип: Имя типа должно быть тСлово, тип= " + str(type(стрИмя))
		assert стрИмя.строка != "", "тТип: Имя типа не должно быть пыстым!"
		сам.__стрИмя = стрИмя # имя типа
		сам.__СловаСекции_Обрезать()

		
		сам.__род = 0 # Род типа -- POINTER TO, ARRAY, RECORD
		сам.__предок = "" # имя предка
		сам.__бЭкспорт = "" # признак экспорта
		сам.__Экспорт_Проверить()
		сам.__Определитель_Проверить()

	def __СловаСекции_Обрезать(сам):
		"""
		Уменьшает слова секции на 1
		"""
		новый_список = {}
		for ключ in range(1, len(сам.__слова_секции)):
			новый_список[ключ-1]=сам.__слова_секции[ключ]
		сам.__слова_секции = {}
		сам.__слова_секции = новый_список
	
	def __Экспорт_Проверить(сам):
		"""
		Проверяет является литип экспортируемым.
		"""
		слово_экспорт = сам.__слова_секции[0]
		assert type(слово_экспорт) == тСлово, "тТип: Признак экспорта должен быть тСлово, тип= " + str(type(слово_экспорт))
		assert слово_экспорт.строка != "", "тТип: Обозначение экспорта типа или определения не может быть пустой строкой"
		if слово_экспорт.строка == "*": # есть экспорт
			сам.__бЭкспорт = True
			сам.__СловаСекции_Обрезать()
	
	def __Определитель_Проверить(сам):
		"""
		Проверяет является ли слово в начале слов секции типа -- "=".
		После обрезания, должно быть первым.
		"""
		слово_опр = сам.__слова_секции[0]
		
		assert слово_опр != тСлово, "тТип: должно быть тСлово, тип="+str(type(слово_опр))
		assert слово_опр.строка != "", "тТип: определение типа не может быть пустым!"
		
		if слово_опр.строка == "=": # если определение типа
			сам.__СловаСекции_Обрезать()
		else: # нарушение выражения
			строка = сам.__корень.исх.строки(слово_опр.коорд.стр)
			print(сам.__корень.исх.строки(слово_опр.коорд.стр), строка)
			сам.ошибка.Коорд("тТип: Отсутствует определитель (=) в объявлении типа", слово_опр.коорд, строка)

	@property
	def имя(сам):
		return сам.__имя

	@property
	def предок(сам):
		return сам.__предок

	@property
	def бЭкспорт(сам):
		return сам.__бЭкспорт

	@property
	def слова(сам):
		return сам.__слова

	def Слово_Доб(сам, пСлово):
		бУсл = type(пСлово) == тСлово
		стрОш = "В слова типа можно добавить только тСлово, type="+str(type(пСлово))
		сам.__корень.конс.Контроль(бУсл, стрОш)

		сам.__слова[len(сам.__слова)] = пСлово
