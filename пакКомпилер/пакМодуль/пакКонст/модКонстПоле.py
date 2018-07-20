# coding:utf8
"""
Содержит тип для разбора констант.
"""

if True:
	from пакКомпилер.пакСлово import тСлово

class тКонстПоле:
	def __init__(сам, пДанные):
		if пДанные['секция'] != "CONST":
			assert False, "тКонстПоле: использование типа не в своей секции, секцйия=" + пДанные['секция']
		сам.слова_секции = пДанные['слова']
		сам.__бЭкспорт = False
		сам.__выраж = {} # Выражение для вычисления константы
		сам.__Имя_Проверить()
		сам.__Экспорт_Проверить()
		сам.__Проверить_Равно()
		сам.__Выраж_Заполнить()

	def __Имя_Проверить(сам):
		"""
		Выясняет правильность имени константы.
		"""
		слово_имя = сам.слова_секции[0]
		имя = слово_имя.Проверить()
		if слово_имя.ЕслиИмя_Строго():
			сам.__имя = имя
			сам.__СловаСекции_Обрезать()
		else:
			assert слово_имя.ЕслиИмя(), "тКонстПоле: имя поля должно быть допустимым именем" + слово_имя.стрИсх

	def __Экспорт_Проверить(сам):
		"""
		Проверяет является ли константа экспортируемой.
		"""
		слово_экспорт = сам.слова_секции[0]
		строка_экспорт = слово_экспорт.Проверить()
		if слово_экспорт.род == тСлово.кУмножить: # есть экспорт
			сам.__бЭкспорт = True
			сам.__СловаСекции_Обрезать()
		elif слово_экспорт.род == тСлово.кРавно:
			pass # это определение константы, дальше присвоение
		else:
			assert False, "тКонстПоле: Символ экспорта допустим '*' или '='" + слово_экспорт.стрИсх

	def __Проверить_Равно(сам):
		"""
		Проверяет литеру равно в константах.
		"""
		слово_равно = сам.слова_секции[0]
		строка_равно = слово_равно.Проверить()
		if слово_равно.род == тСлово.кРавно: # есть уравнивание
			сам.__СловаСекции_Обрезать()
		else:
			assert False, "тКонстПоле: Символ приравнивания должен быть '='" + слово_равно.стрИсх

	def __Выраж_Заполнить(сам):
		"""
		Пока не встретится ";" -- заполнять выражение
		"""
		слово_равно = сам.слова_секции[0]
		строка_равно = слово_равно.Проверить()
		while not (слово_равно.род == тСлово.кТочкаЗапятая):
			сам.__СловаСекции_Обрезать()
			сам.__выраж[len(сам.__выраж)] = строка_равно
			слово_равно = сам.слова_секции[0]
			строка_равно = слово_равно.Проверить()
		сам.__СловаСекции_Обрезать() # Откидываем завершающий разделитель

	def __СловаСекции_Обрезать(сам):
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список = {}
		for ключ in range(1, len(сам.слова_секции)):
			новый_список[ключ-1]=сам.слова_секции[ключ]
		сам.слова_секции = {}
		сам.слова_секции = новый_список
