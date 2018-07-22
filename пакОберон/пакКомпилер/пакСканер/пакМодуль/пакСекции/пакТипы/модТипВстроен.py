# coding:utf8
"""
Модуль описывает тип-алиас встроенного типа.
"""

if True:
	from .модРод import тРод
	from ....пакСлово import тСлово
	from . модТипБазовый import тТипБазовый

class тТипВстроен(тТипБазовый):
	def __init__(сам, пДанные):
		тТипБазовый.__init__(сам, пДанные)

		сам.__Тип_Проверить()
		сам.Разделитель_Обрезать()

	def __Тип_Проверить(сам):
		"""
		Проверяет не является ли тип алиасом встроенного типа.
		Сейчас у сам.тип выставлено слово, описывающее его тип-алиас
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
			assert False, "тТипАлиас: неизвестный встроенный предок" + слово_тип.стрИсх
		# обрежем род типа
		сам.СловаСекции_Обрезать()
