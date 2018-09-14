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
		сканер = тСканер(сам.__оберон, пФайлИсхИмя)
		if сам.__конс.бОшВнутр:
			сам.__конс.ОшВнутр("тКомпилер.Выполнить(): внутренняя ошибка сканера")
			return
		if сам.__конс.бОшибка:
			сам.__конс.Ошибка("тКомпилер.Выполнить(): ошибка исходника при работе сканера")
			return

		анализ = тАнализ(сам.__оберон, сканер.Секции_Получить())
		if сам.__конс.бОшВнутр:
			сам.__конс.ОшВнутр("тКомпилер.Выполнить(): внутренняя ошибка анализа")
			return
		if сам.__конс.бОшибка:
			сам.__конс.Ошибка("тКомпилер.Выполнить(): ошибка исходника при работе анализа")
			return

		разбор = тРазбор(анализ.данные)
		if сам.__конс.бОшВнутр:
			сам.__конс.ОшВнутр("тКомпилер.Выполнить(): внутренняя ошибка разбора")
			return
		if сам.__конс.бОшибка:
			сам.__конс.Ошибка("тКомпилер.Выполнить(): ошибка исходника при работе разбора")
			return
