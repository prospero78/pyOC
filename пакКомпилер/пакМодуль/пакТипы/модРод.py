# coding:utf8
"""
Описывает род описываемого типа.
Может быть без_типа, встроенный, ARRAY, POINTER, RECORD
"""

class тРод:
	сБезТипа = "без_типа"
	сВстроен = "встроенный"
	сМассив = "ARRAY"
	сЗапись = "RECORD"
	сУказатель = "POINTER"
	сПроцедура = "PROCEDURE"
	сБезПредка = "без_предка"
	сБулево = "BOOLEAN"
	тип_встроен = ["BOOLEAN", "CHAR", "INTEGER", "REAL", "BYTE", "SET"]

	def __init__(сам):
		pass
