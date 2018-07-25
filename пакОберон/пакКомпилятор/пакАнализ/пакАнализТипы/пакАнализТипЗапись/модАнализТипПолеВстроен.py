# coding: utf8
"""
Модуль предоставляеттип для полей в секции типов.
Анализирует встроенные типы полей.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод
	from .модАнализТипПолеБазовый import тАнализТипПолеБазовый

class тАнализТипПолеВстроен(тАнализТипПолеБазовый):
	def __init__(сам, пДанные):
		тАнализТипПолеБазовый.__init__(сам, пДанные)
		#сам.ИмяПоле_Проверить()
		#сам.бЭкспорт_Проверить()
		#сам.Двоеточие_Обрезать()
		сам.__ВстроенТип_Проверить()
		# Здесь нет END -- сразу ";"
		сам.Разделитель_Обрезать()
		слово = сам.слова_секции[0]
		print("тАнализТипПолеВстроен: 4056 после обрезки разделителя",слово.стрИсх)

	def __ВстроенТип_Проверить(сам):
		"""
		Проверяет ,является ли тип поля встроенным.
		Проверяет не является ли тип алиасом встроенного типа.
		Сейчас сам.тип выставлено слово, описывающее его тип-алиас
		"""
		слово_тип = сам.слова_секции[0]
		строка_тип = слово_тип.Проверить()
		if строка_тип == "BOOLEAN":
			сам.Предок_Уст("BOOLEAN")
		elif строка_тип == "CHAR":
			сам.Предок_Уст("CHAR")
		elif строка_тип == "INTEGER":
			сам.Предок_Уст("INTEGER")
		elif строка_тип == "REAL":
			сам.Предок_Уст("REAL")
		elif строка_тип == "BYTE":
			сам.Предок_Уст("BYTE")
		elif строка_тип == "SET":
			сам.Предок_Уст("SET")
		else:
			assert False, "тАнализТипПолеВстроен: неизвестный встроенный предок" + слово_тип.стрИсх
		# обрежем род типа
		сам.СловаСекции_Обрезать()
		print("тАнализТипПолеВстроен: 8993 встроенный тип=", строка_тип, слово_тип.стрИсх)
