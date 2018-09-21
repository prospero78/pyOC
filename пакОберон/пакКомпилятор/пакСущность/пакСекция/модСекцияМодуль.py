# coding:utf8
"""
Жёстко прописанная секция MODULE
"""
if True:
	from .модСекция import тСекция
	from пакОберон.пакКомпилятор.пакСущность.пакОшибка import тОшибка

class тСекцияМодуль(тСекция):
	__slots__ = ("__конс", "ошм")
	def __init__(сам, пОберон, пДанные):
		сам.__конс = пОберон.конс
		сам.__конс.Отладить("тСекцияМодуль.__init__()")

		сам.ошм = тОшибка(пОберон, "тСекцияМодуль")

		тСекция.__init__(сам, пОберон, пДанные)
		if сам.ошс.бВнутр:
			сам.ошм.Внутр("__init__()", "При наследовании тСекция")
			return
		if сам.ошс.бИсх:
			сам.ошм.Исх("__init__()", "При наследовании тСекция")
			return

		if пДанные['секция'] != "MODULE":
			сам.ошм.Исх("__init__()", "Ошибочное использование типа в секции MODULE, секция=" + пДанные['слова'])
			return
