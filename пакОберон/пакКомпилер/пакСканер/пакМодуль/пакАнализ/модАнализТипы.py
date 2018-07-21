# coding: utf8
"""
Модуль обеспечивает анализ секции типов.
"""


if True:
	from ...пакМодуль.пакСекция import тСекцияТипы

class тАнализТипы(тСекцияТипы):
	def __init__(сам, пДанные):
		тСекцияТипы.__init__(сам, пДанные)
		сам.__конст = {} # Содержит словарь для констант
		сам.__Обработать()

	def __Слово_TYPE_Обрезать(сам):
		"""
		Первое слово в списке слов должно быть TYPE.
		Если нет -- значит в исходнике нет описания типов.
		Возвращает результат встречи с TYPE
		"""
		слово = сам.слова_модуля[0]
		if слово.строка =='TYPE':
			# укоротить типы
			слова = {}
			for счёт in range(1, len(сам.слова_модуля)):
				слово = сам.слова_модуля[счёт]
				слова[счёт-1] = слово
			сам.слова_модуля = {}
			сам.слова_модуля = слова
			сам.бСекцияЕсть = True
		else:
			assert False, "тАнализТипы: секция должна начинаться с TYPE" + слово.стрИсх


	def __Обработать(сам):
		"""
		Вся обработка типов заключена здесь.
		"""
		сам.__Слово_TYPE_Обрезать()

	@property
	def типы(сам):
		return сам.__типы
