# coding:utf8
"""
Жёстко прописанная секция IMPORT
"""
if True:
	from .модСекция import тСекция

class тСекцияТипы(тСекция):
	def __init__(сам, пОберон,пДанные):
		сам.__оберон = пОберон
		сам.__конс = пОберон.конс
		сам.__конс.Отладить("тСекцияТипы.__init__()")

		сам.__бОшВнутр = False

		тСекция.__init__(сам, пОберон, пДанные)
		if сам.бОшВнутр_Секция:
			сам.__бОшВнутр = True
			return
		if пДанные['секция'] != "TYPE":
			сам.__бОшВнутр = True
			сам.__конс.ОшВнутр("тСекцияТипы.__init__(): ошибка компилятора. Ошибочное использование типа в секции TYPE, секция=" + пДанные['слова'])
			return

	@property
	def бОшВнутр_СекцияТипы(сам):
		return сам.__бОшВнутр
