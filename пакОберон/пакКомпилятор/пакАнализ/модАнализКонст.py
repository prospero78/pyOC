# coding: utf8
"""
Модуль анализирует секцию слов констант
"""

if True:
	from .модАнализБаза import тАнализБаза
	from .пакАнализКонстанты import тКонстПоле

class тАнализКонст(тАнализБаза):
	def __init__(сам, пДанные:dict):
		тАнализБаза.__init__(сам, пДанные)
		сам.__конст = {} # Содержит словарь для констант
		сам.__модуль_имя = пДанные['модуль_имя']
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
			парам['модуль_имя'] = сам.__модуль_имя
			конст = None
			конст = тКонстПоле(парам)
			сам.__конст[len(сам.__конст)] = конст
			сам.слова_секции = {}
			сам.слова_секции = конст.слова_секции

	def КонстСекции_Печать(сам):
		"""
		Печатает все константы секции через паспорт константы
		"""
		print("Секция констант. Всего констант", len(сам.__конст))
		for ключ in сам.__конст:
			сам.__конст[ключ].Паспорт_Печать()

	@property
	def константы(сам) -> dict:
		return сам.__конст
