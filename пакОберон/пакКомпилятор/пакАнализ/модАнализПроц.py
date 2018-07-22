# coding: utf8
"""
Модуль предоставляет тип для анализа секции переменных
"""
if True:
	from .модАнализБаза import тАнализБаза

class тАнализПроц(тАнализБаза):
	def __init__(сам, пДанные):
		тАнализБаза.__init__(сам, пДанные)
		сам.__проц = {} # Содержит словарь для констант
		сам.__Процедуры_Разделить()

	def __Процедуры_Разделить(сам):
		"""
		Пока не исчерпаны слова секции -- последовательно вызываем новую процедуру.
		"""
		while len(сам.слова_секции) > 0:
			парам = {}
			парам['секция'] = "PROCEDURE" # Прикидываемся, что это исключительно процедуры
			парам['слова'] = сам.слова_секции
			парам['имя'] = ""
			парам['бЭкспорт'] = False
			перем = None
			перем = тАнализПроцедура(парам)
			#перем.Паспорт_Печать()
			сам.слова_секции = {}
			сам.слова_секции = перем.слова_секции
			сам.__перем[len(сам.__перем)] = перем

	@property
	def процедуры(сам):
		return сам.__проц
