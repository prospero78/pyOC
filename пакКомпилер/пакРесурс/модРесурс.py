# coding: utf8
"""
Содержит класс ресурсов.
"""

class тРесурс:
	def __init__(сам, корень):
		сам.__корень = корень
		сам.app     = {}
		сам.winMain = {}
		сам.Шапка_Уст()
		сам.Язык_Уст()
	
	def Шапка_Уст(сам):
		сам.app['date']  = "2018-07-05"
		сам.app['time']  = "20:25"
		сам.app['build'] = "Build"
		сам.app['build_num'] = "059"
		
	def Язык_Уст(сам, lang = "ru"):
		if True:
			сам.app['name'] = 'Oberon-07 Compiler'
			сам.winMain['log'] = 'Log'
			сам.winMain['mnuFile'] = 'File'
			сам.winMain['mnuExit'] = 'Exit'
			сам.winMain['mnuOpen'] = 'Open...'
			
		if lang == "ru":
			сам.Компиляция = "Компиляция"
			сам.app['name']  = 'Компилятор Oberon-07'
			сам.app['name1'] = 'Oberon-07'
			сам.app['build'] = "Cборка"
			сам.winMain['log'] = 'Лог'
			сам.winMain['mnuFile'] = 'Файл'
			сам.winMain['mnuExit'] = 'Выход'
			сам.winMain['mnuOpen'] = 'Отрыть...'
