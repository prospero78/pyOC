# coding: utf8
"""
Содержит класс ресурсов.
"""

class тРесурс:
	def __init__(сам, пКорень):
		сам.__корень = пКорень
		сам.app     = {}
		сам.winMain = {}
		сам.Шапка_Уст()
		сам.Язык_Уст()

	def Шапка_Уст(сам):
		сам.app['date']  = "2018-09-19"
		сам.app['time']  = "15:47"
		сам.app['build'] = "Сборка"
		сам.app['build_num'] = "1102"

	def Язык_Уст(сам, lang = "ru"):
		if True:
			сам.app['name'] = 'Oberon-07 Compiler'
			сам.winMain['log'] = 'Log'
			сам.winMain['mnuFile'] = 'File'
			сам.winMain['mnuExit'] = 'Exit'
			сам.winMain['mnuOpen'] = 'Open...'

		if lang == "ru":
			сам.компиляция = "Компиляция "
			сам.app['name']  = 'Компилятор Oberon-07'
			сам.app['name1'] = '\u262d Oberon-07'
			сам.app['build'] = "Cборка"
			сам.winMain['log'] = 'Лог'
			сам.winMain['mnuFile'] = 'Файл'
			сам.winMain['mnuAnaliz'] = 'Анализ'
			сам.winMain['mnuExit'] = 'Выход'
			сам.winMain['mnuOpen'] = 'Отрыть...'
			сам.winMain['mnuHelp'] = 'Справка'
			сам.winMain['mnuHelpShow'] = 'Показать справку...'
