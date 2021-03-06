# coding:utf8
"""
Описывает род описываемого типа.
Может быть без_типа, встроенный, ARRAY, POINTER, RECORD
"""

class тРод:
	сБезРода = "без_рода"
	сБезТипа = "без_типа"
	сВстроен = "встроенный"
	сМассив = "ARRAY"
	сЗапись = "RECORD"
	сУказатель = "POINTER"
	сПроцедура = "PROCEDURE"
	сБезПредка = "без_предка"
	сЧастный = "частный"
	сБулево = "BOOLEAN"
	тип_встроен = [сБулево, "SET", "BYTE", "CHAR", "INTEGER", "REAL"]

	def __init__(сам, пРод:str):
		сам.__стрРод = пРод #type:str
		сам.__цРод = -1	#type:int

		if пРод == "":
			сам.__цРод = тРод.сБезРода
		elif пРод == тРод.сМассив:
			сам.__цТип = 0

	@property
	def цРод(сам):
		"""
		Возвращает числовое згачение рода слова
		"""
		return сам.__цТип
