# coding: utf8
"""
Модуль базового типа для анализа секции для всех секций
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from .модАнализИмпорт import тАнализИмпорт
	from .модАнализКонст import тАнализКонст
	from .модАнализТипы import тАнализТипы
	from .модАнализПерем import тАнализПерем

class тАнализ:
	def __init__(сам, пОберон, пДанные:dict)->None:
		def Анализ_Проверить()->None:
			бУсл :bool= пДанные['анализ'] == "анализ"
			стрОш :str= "В секцию  должен передаваться словарь слов для анализа"
			assert бУсл, стрОш

		сам.__оберон = пОберон
		сам.__конс = пОберон.конс
		if True: # слова секций
			Анализ_Проверить()
			сам.__анализ :str= пДанные['анализ']
			сам.слова_импорта :dict= пДанные['импорт'] # все слова секции импорт
			сам.слова_конст :dict= пДанные['константы'] # все слова секции констант
			сам.слова_типы :dict= пДанные['типы'] # все слова секции типов
			сам.слова_перем :dict= пДанные['переменные'] # все слова секции переменных
			сам.слова_проц :dict= пДанные['процедуры'] # все слова секции процедур
			сам.слова_модуля :dict= пДанные['модуль'] # все слова инициализации модуля
			#сам.бСекцияЕсть = False # Признак наличия секции
			#сам.__слово_конец = None # последнее слово в секции

		парам :dict= {}
		парам['анализ'] = "анализ"
		if True: # анализ импорта
			парам['слова']  = сам.слова_импорта
			импорт :тАнализИмпорт= тАнализИмпорт(пОберон, парам)
			if сам.__конс.бОшВнутр:
				сам.__конс.ОшВнутр("тАнализ.__init__(): ошибка компилятора при анализе импорта")
				return
			сам.модули = импорт.модули
			#импорт.МодулиСекции_Печать()

		if True: # анализ констант
			парам['слова']  = сам.слова_конст
			парам['модуль_имя'] = пДанные['модуль_имя']
			конст :тАнализКонст= тАнализКонст(пОберон, парам)
			сам.константы = конст.константы
			#конст.КонстСекции_Печать()

		if True: # анализ типов
			парам['слова']  = сам.слова_типы
			типы :тАнализТипы= тАнализТипы(пОберон, парам)
			#типы.ПроцСекции_Печать()

		if True: # анализ переменных
			парам['слова']  = сам.слова_перем
			перем :тАнализПерем= тАнализПерем(парам)
			#прем.ПроцСекции_Печать()

	@property
	def данные(сам)->dict:
		данные :dict= {}
		данные['конст'] = сам.константы
		return данные
