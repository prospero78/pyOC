# coding: utf8
"""
Модуль предоставляет тип для хранения имени модуля и его алиаса.
"""

if True:
	from пакКомпилер.пакСлово import тСлово

class тМодуль:
	def __init__(сам, пСекция):
		сам.__секция = пСекция
		сам.__алиас = "" # Алиас модуля
		сам.__имя = ""   # Настоящее имя модуля
		if сам.__Проверить_Равно():     # проверка на наличие алиаса
			сам.__Алиас_Получить()
			сам.__СловаСекции_Обрезать() # литера равно -- признак алиаса
			сам.__Имя_Получить()         # сложное имя при наличии алиаса
		сам.__Имя_Проверить()

	def __Имя_Получить(сам):
		"""
		Пока не встретится "," или ";" -- заполнять имя алиаса
		"""
		слово_равно = сам.__секция.слова_секции[0]
		имя = слово_равно.Проверить()
		if имя != ".":
			while имя.ЕслиСтр_Допустимо() and (not (слово_равно.род in [тСлово.кЗапятая, тСлово.кТочкаЗапятая])):
				сам.__СловаСекции_Обрезать()
				сам.__имя[len(сам.__выраж)] = строка_равно
				строка_равно = сам.__Слово_Проверить()
				слово_равно = сам.__секция.слова_секции[0]
			сам.__СловаСекции_Обрезать() # Откидываем завершающий разделитель
		else:
			assert False, "тМодуль: имя модуля не может начинаться с точки" + слово_равно.стрИсх

	def __Алиас_Получить(сам):
		"""
		Выясняет правильность имени модуля.
		"""
		слово_имя = сам.__секция.слова_секции[0]
		имя = слово_имя.Проверить()
		if слово_имя.ЕслиИмя_Строго():
			сам.__имя = имя
			сам.__СловаСекции_Обрезать()
		else:
			assert False, "тМодуль: алиас модуля должно быть допустимым именем, имя=" + имя + слово_имя.стрИсх

	def __Проверить_Равно(сам):
		"""
		Проверяет литеру равно в импорте модулей. Может и не быть
		В словаре слов-- это по счёту ВТОРОЕ слово
		"""
		бРезульт = False
		слово_равно = сам.__секция.слова_секции[1]
		строка_равно = слово_равно.Проверить()
		if слово_равно.род == тСлово.кРавно: # есть уравнивание
			бРезульт = True
		return бРезульт

	def __Имя_Проверить(сам):
		"""
		Пока не встретится "," или ";" -- заполнять имя алиаса
		"""
		слово_равно = сам.__секция.слова_секции[0]
		строка_равно = слово_равно.Проверить()
		while not (слово_равно.род in [тСлово.кЗапятая, тСлово.кТочкаЗапятая]):
			сам.__СловаСекции_Обрезать()
			сам.__имя += строка_равно
			слово_равно = сам.__секция.слова_секции[0]
			строка_равно = слово_равно.Проверить()
		сам.__СловаСекции_Обрезать() # Откидываем завершающий разделитель

	def __СловаСекции_Обрезать(сам):
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список = {}
		for ключ in range(1, len(сам.__секция.слова_секции)):
			новый_список[ключ-1]=сам.__секция.слова_секции[ключ]
		сам.__секция.слова_секции = {}
		сам.__секция.слова_секции = новый_список

	@property
	def алиас(сам):
		return сам.__алиас

	@property
	def имя(сам):
		return сам.__стрИмя

	@property
	def бАлиас(сам):
		бАлиас = False
		if сам.__стрАлиас != "":
			бАлиас = True
		return бАлиас

	@property
	def номер(сам):
		return сам.__цНомер
