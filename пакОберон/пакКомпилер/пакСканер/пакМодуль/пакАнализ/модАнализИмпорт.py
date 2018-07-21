# coding: utf8
"""
Модуль предоставляет тип для анализа секции импорта
"""

if True:
	#from ....пакСлово import тСлово
	from .модИмпортМодуль import тИмпортМодуль
	from ...пакМодуль.пакСекция import тСекцияИмпорт


class тАнализИмпорт(тСекцияИмпорт):
	def __init__(сам, пДанные):
		тСекцияИмпорт.__init__(сам, пДанные)
		сам.__модули = {} # Содержит словарь для импорта модулей
		сам.__Импорт_Разобрать()

	def __Импорт_Разобрать(сам):
		"""
		Делает разбор импорта, вычисляет алиасы.
		"""
		while len(сам.слова_секции) > 0:
			парам = {}
			парам['секция'] = "IMPORT"
			парам['слова'] = сам.слова_секции

			имп_модуль = None
			имп_модуль = тИмпортМодуль(парам)
			сам.__модули[сам.цМодулиВсего] = имп_модуль

			сам.слова_секции =  {}
			сам.слова_секции = имп_модуль.слова_секции

	@property
	def модули(сам):
		return сам.__модули

	@property
	def цМодулиВсего(сам):
		return len(сам.__модули)
