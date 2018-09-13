# coding: utf8
"""
Модуль "Компилер".
Содержит в себе все составляющие для компилятора Оберона
"""
if True:

	from .пакСканер import тСканер
	from .пакАнализ import тАнализ
	from .пакРазбор import тРазбор

class тКомпилер:
	def __init__(сам, пОберон)->None:
		сам.__оберон = пОберон
		сам.__конс = пОберон.конс

	def Выполнить(сам, пФайлИсхИмя:str):
		#TODO: доделать контроль на внутреннее состояние ошибки
		сканер = тСканер(сам.__оберон, пФайлИсхИмя)
		if сам.__конс.бОшибка:
			сам.__конс.ОшВнутр("тКомпилер.Выполнить(): внутренняя ошибка")
			return
		анализ = тАнализ(сам.__оберон, сканер.Секции_Получить())
		разбор = тРазбор(анализ.данные)
