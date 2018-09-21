# coding: utf8
"""
Предоставляет тип сканера для обработки текста на входе.
Сканер служит для первичного сканирования текста.
Он же проверяет правильность поступления слов из исходного текста.
"""
if True:
	from .пакСканерИсходник import тСканерИсходник
	from .пакСканерМодуль import тСканерМодуль
	from .пакСканерИмпорт import тСканерИмпорт
	from .пакСканерКонстанты import тСканерКонстанты
	from .пакСканерТипы import тСканерТипы
	from .пакСканерПеременные import тСканерПеременные
	from .пакСканерПроцедуры import тСканерПроцедуры
	from пакОберон.пакКомпилятор.пакСущность.пакОшибка import тОшибка

	from typing import Dict as тСловарь # словарь для контроля типов
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово

class тСканер:
	def __init__(сам, пОберон, пФайлИмяИсх:str) -> None:
		сам.__конс = пОберон.конс
		сам.__конс.Отладить("тСканер.__init__()")

		сам.ош = тОшибка(пОберон, "тСканер")

		сам.__импорт :dict= {} # тСловарь[]##
		сам.__конст  :dict= {} ##
		сам.__типы   :dict= {} ##   Группа словарей, хранит группы слов по секциям
		сам.__перем  :dict= {} ##    для дальнейшего анализа
		сам.__проц   :dict= {} ##
		сам.__модуль :dict= {} ##
		сам.__модуль_имя :str= "" # Имя модуля в котором производятся операции

		if type(пФайлИмяИсх) != str:
			стрОш = "пФайлИсх должен быть str, type="+str(type(пФайлИмяИсх))
			сам.ош.Внутр("__init__()", стрОш)
			return

		if пФайлИмяИсх =="":
			пФайлИмяИсх = "Hello.o7"
		сам.исх    = тСканерИсходник(пОберон, пФайлИмяИсх)
		сам.модуль = тСканерМодуль(пОберон)

		парам = модуль.Парам_Получ()
		парам['секция'] = "IMPORT"
		импорт = тСканерИмпорт(пОберон, парам)
		if импорт.ош_.бВнутр:
			сам.ош.Внутр("__init__()", "При создании тСканерИмпорт")
			return
		if импорт.ош_.бИсх:
			сам.ош.Исх("__init__()", "При создании тСканерИмпорт")
			return
		сам.__импорт = импорт.слова_секции
		сам.слова_модуля :dict= {}
		сам.слова_модуля = импорт.слова_модуля

		парам = импорт.Парам_Получ()
		парам['секция'] = "CONST"
		парам['модуль_имя'] = модуль.имя
		конст = тСканерКонстанты(пОберон, парам)
		if конст.ошк.бВнутр:
			сам.ош.Внутр("__init__()", "При создании тСканерКонстанты")
			return
		if конст.ошк.бИсх:
			сам.ош.Исх("__init__()", "При создании тСканерКонстанты")
			return
		сам.__конст = конст.слова_секции
		сам.слова_модуля = {}
		сам.слова_модуля = конст.слова_модуля

		парам = конст.Парам_Получ()
		парам['секция'] = "TYPE"
		типы = тСканерТипы(пОберон, парам)
		if типы.ошт.бВнутр:
			сам.ош.Внутр("__init__()", "При создании тСканерТипы")
			return
		if типы.ошт.бИсх:
			сам.ош.Исх("__init__()","При создании тСканерТипы")
			return
		сам.__типы = типы.слова_секции
		сам.слова_модуля = {}
		сам.слова_модуля = типы.слова_модуля

		парам = типы.Парам_Получ()
		парам['секция'] = "VAR"
		перем = тСканерПеременные(пОберон, парам)
		if перем.ош_с.бВнутр:
			сам.ош.Внутр("__init__()", "При создании тСканерПеременные")
			return
		if перем.ош_с.бИсх:
			сам.ош.Исх("__init__()", "При создании тСканерПеременные")
			return
		сам.__перем = перем.слова_секции
		сам.слова_модуля = {}
		сам.слова_модуля = перем.слова_модуля

		парам = перем.Парам_Получ()
		парам['секция'] = "PROCEDURE"
		процедуры = тСканерПроцедуры(пОберон, парам)
		if процедуры.ош_п.бВнутр:
			сам.ош.Внутр("__init__()", "При создании тСканерПроцедуры")
			return
		if процедуры.ош_п.бИсх:
			сам.ош.Исх("__init__()", "При создании тСканерПроцедуры")
			return
		сам.__проц = процедуры.слова_секции
		сам.слова_модуля = {}
		сам.слова_модуля = процедуры.слова_секции

		сам.__модуль = процедуры.слова_модуля

	def Секции_Получить(сам) -> dict:
		парам = {}
		парам['импорт']    = сам.__импорт
		парам['константы'] = сам.__конст
		парам['типы']      = сам.__типы
		парам['переменные']= сам.__перем
		парам['процедуры'] = сам.__проц
		парам['модуль']    = сам.__модуль
		парам['анализ']    = "анализ" #type:ignore
		парам['модуль_имя']= сам.__модуль_имя #type:ignore
		return парам

	def Обработать(сам):
		"""
		Выполняет обработку исходника в пакетном режиме
		(не по шагам).
		"""
		сам.исх.Обработать()
		if сам.исх.ош.бВнутр:
			сам.ош.Внутр("__init__()", "При создании тСканерИсходник")
			return
		if сам.исх.ош.бИсх:
			сам.ош.Исх("__init__()", "При создании тСканерИсходник")
			return

		сам.модуль.Обработать(сам.исх.Парам_Получ())
		if модуль.ош_.бВнутр:
			сам.ош.Внутр("__init__()", "При создании тСканерМодуль")
			return
		if модуль.ош_.бИсх:
			сам.ош.Исх("__init__()", "При создании тСканерМодуль")
			return
		сам.__модуль_имя = модуль.имя

	def Шаг(сам):
		"""
		Выполняет сканирование исходника по шагам.
		"""
		if not сам.исх.бСловоГотово:
			сам.исх.Шаг()
			return
		if not сам.модуль.бМодульГотово:
			сам.исх.Шаг()
			return
