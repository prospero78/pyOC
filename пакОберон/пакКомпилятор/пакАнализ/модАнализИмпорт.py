# coding: utf8
"""
Модуль предоставляет тип для анализа секции импорта
"""

if True:
	from .модАнализБаза import тАнализБаза
	from .пакАнализИмпорт import тАнализМодуль

class тАнализИмпорт(тАнализБаза):
	def __init__(сам, пОберон, пДанные:dict)->None:
		сам.__оберон = пОберон
		сам.__конс = пОберон.конс
		тАнализБаза.__init__(сам, пОберон, пДанные)
		сам.__модули :dict= {} # Содержит словарь для импорта модулей
		сам.__Импорт_Разобрать()

	def __Импорт_Разобрать(сам)->None:
		"""
		Делает разбор импорта, вычисляет алиасы.
		"""
		while len(сам.слова_секции) > 0:
			парам :dict= {}
			парам['секция'] = "IMPORT"
			парам['слова_секции'] = сам.слова_секции
			парам['слова'] = {}
			#имп_модуль = None
			имп_модуль :тАнализМодуль = тАнализМодуль(сам.__оберон, парам)
			сам.__модули[сам.цМодулиВсего] = имп_модуль

			сам.слова_секции =  {}
			сам.слова_секции = имп_модуль.слова_секции

	def МодулиСекции_Печать(сам):
		сам.__конс.Отладить("тАнализИмпорт: модули секции IMPORT. Всего модулей=" + str(len(сам.модули)))
		for ключ in сам.__модули:
			модуль = сам.__модули[ключ]
			модуль.Паспорт_Печать()
	@property
	def модули(сам)->dict:
		return сам.__модули

	@property
	def цМодулиВсего(сам)->int:
		return len(сам.__модули)
