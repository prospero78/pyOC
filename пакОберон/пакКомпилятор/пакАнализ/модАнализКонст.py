# coding: utf8
"""
Модуль анализирует секцию слов констант
"""

if True:
	from .модАнализБаза import тАнализБаза
	from .пакАнализКонстанты import тКонстПоле

class тАнализКонст(тАнализБаза):
	def __init__(сам, пОберон, пДанные:dict)->None:
		сам.__оберон = пОберон
		сам.__конс = пОберон.конс
		сам.__конс.Отладить("тАнализБаза.__init__()")

		сам.__бОшВнутр = False

		тАнализБаза.__init__(сам, пОберон, пДанные)
		if сам.бОшВнутр_АнализБаза:
			сам.__бОшВнутр = True
			стрОш = "тАнализКонст.__init__(): ошибка компилятора. При вызове тАнализБаза"
			сам.__конс.ОшВнутр("стрОш")
			return
		сам.__конст :dict= {} # Содержит словарь для констант
		сам.__модуль_имя = пДанные['модуль_имя']
		сам.__Константы_Разбить()

	def __Константы_Разбить(сам):
		"""
		Теперь слова секции групируем в константы
		"""
		цСчётСлова = 0 # Счётчик констант
		счёт = 0
		while сам.цСловаСекции > 1:
			парам = {}
			парам['секция'] = "CONST"
			парам['слова'] = сам.слова_секции
			парам['модуль_имя'] = сам.__модуль_имя
			конст = None
			конст = тКонстПоле(сам.__оберон, парам)
			if конст.бОшВнутр:
				сам.__бОшВнутр = True
				стрОш = "тАнализКонст: ошибка компилятора. При вызове тКонстПоле"
				сам.__конс.ОшВнутр(стрОш)
				return
			if конст.бОшИсх:
				сам.__бОшИсх = True
				стрОш = "тАнализКонст: ошибка исходника. При вызове тКонстПоле"
				сам.__конс.ОшВнутр(стрОш)
				return
			сам.__конст[len(сам.__конст)] = конст
			сам.слова_секции = {}
			сам.слова_секции = конст.слова_секции

	def КонстСекции_Печать(сам):
		"""
		Печатает все константы секции через паспорт константы
		"""
		сам.__конс.Печать("Секция констант. Всего констант"+str(len(сам.__конст)))
		for ключ in сам.__конст:
			сам.__конст[ключ].Паспорт_Печать()

	@property
	def константы(сам) -> dict:
		return сам.__конст

	@property
	def бОшВнутр(сам):
		return сам.__бОшВнутр
