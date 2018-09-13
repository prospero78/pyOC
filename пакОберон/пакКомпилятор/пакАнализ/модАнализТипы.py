# coding: utf8
"""
Модуль обеспечивает анализ секции типов.
"""

if True:
	from .модАнализБаза import тАнализБаза
	from .пакАнализТипы import тАнализТип

class тАнализТипы(тАнализБаза):
	def __init__(сам, пОберон, пДанные):
		тАнализБаза.__init__(сам, пОберон, пДанные)
		сам.__типы = {} # Содержит описания типов
		сам.__Обработать()

	def __Слово_TYPE_Обрезать(сам):
		"""
		Первое слово в списке слов должно быть TYPE.
		Если нет -- значит в исходнике нет описания типов.
		Возвращает результат встречи с TYPE
		"""
		слово = сам.слова_секции[0]
		if слово.строка =='TYPE':
			# укоротить типы
			слова = {}
			for счёт in range(1, len(сам.слова_секции)):
				слово = сам.слова_секции[счёт]
				слова[счёт-1] = слово
			сам.слова_секции = {}
			сам.слова_секции = слова
			сам.бСекцияЕсть = True
		else:
			assert False, "тАнализТипы: секция должна начинаться с TYPE" + слово.стрИсх

	def __Обработать(сам):
		"""
		Вся обработка типов заключена здесь.
		"""
		сам.__Слово_TYPE_Обрезать()
		while len(сам.слова_секции) > 1:
			парам = {}
			парам['слова'] = сам.слова_секции
			парам['секция']= "анализ"
			парам['имя'] = ""
			парам['бЭкспорт'] = False
			тип = тАнализТип(парам)
			сам.слова_секции = тип.слова_секции
			сам.__типы[len(сам.__типы)] = тип

	def ПроцСекции_Печать(сам):
		print("Всего слов в секции типов:", len(сам.слова_секции))
		print("Типы секции: всего типов =", len(сам.__типы), "\n")
		for ключ in сам.__типы:
			сам.__типы[ключ].Паспорт_Печать()
		print

	@property
	def типы(сам):
		return сам.__типы
