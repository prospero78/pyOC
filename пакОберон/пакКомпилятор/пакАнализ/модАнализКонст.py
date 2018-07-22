# coding: utf8
"""
Модуль анализирует секцию слов констант
"""

if True:
	from .модАнализ import тАнализ
	from .пакАнализКонстанты import тКонстПоле

class тАнализКонст(тАнализ):
	def __init__(сам, пДанные):
		тСекцияКонст.__init__(сам, пДанные)
		сам.__конст = {} # Содержит словарь для констант
		сам.__Константы_Разбить()

	def __Константы_Разбить(сам):
		"""
		Теперь слова секции групируем в константы
		"""
		цСчётСлова = 0 # Счётчик констант
		счёт = 0
		while сам.цСловаСекции > 1:
			парам = {}
			парам['секция'] = "CONST"
			парам['слова'] = сам.слова_секции

			конст = None
			конст = тКонстПоле(парам)
			сам.__конст[len(сам.__конст)] = конст
			сам.слова_секции = {}
			сам.слова_секции = конст.слова_секции

	@property
	def константы(сам):
		сам.__конст
