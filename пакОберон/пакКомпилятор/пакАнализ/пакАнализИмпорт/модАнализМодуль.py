# coding: utf8
"""
Модуль предоставляет тип для хранения имени модуля и его алиаса.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакСекция import тСекцияИмпорт
	from пакОберон.пакКомпилятор.пакСущность.пакОшибка import тОшибка

class тАнализМодуль(тСекцияИмпорт):
	def __init__(сам, пОберон, пДанные:dict)->None:
		сам.__оберон = пОберон
		сам.__конс = пОберон.конс
		сам.__конс.Отладить("тАнализМодуль.__init__()")

		сам.ошм = тОшибка(пОберон, "тАнализМодуль")

		тСекцияИмпорт.__init__(сам, пОберон, пДанные)
		if сам.оши.бВнутр:
			сам.ошм.Внутр("__init__()", "При создании предка тСекцияИмпорт")
			return
		#сам.СловаСекции_Печать()
		сам.__стрАлиас :str= "" # Алиас модуля
		сам.__алиас_слово :тСлово # тСлово алиаса
		сам.__имя :str= "" # Настоящее имя модуля
		if сам.__Проверить_Присвоить():     # проверка на наличие алиаса
			сам.__Алиас_Получить()
			сам.__СловаСекции_Обрезать() # литера равно -- признак алиаса
		сам.__Имя_Проверить()  # сложное имя в любом случае алиаса

	def __Алиас_Получить(сам)->None:
		"""
		Выясняет правильность имени модуля.
		"""
		слова_алиас :тСлово= сам.слова_секции[0]
		if слова_алиас.ЕслиИмя_Строго():
			#TODO: сделать отдельный тип для сущности модуля
			сам.__стрАлиас = слова_алиас.строка
			сам.__алиас_слово = слова_алиас
			сам.__СловаСекции_Обрезать()
		else:
			сам.ошм.Внутр("__Алиас_Получить()", "Алиас модуля должно быть допустимым именем, имя=" + алиас + слова_алиас.стрИсх)
			return

	def __Проверить_Присвоить(сам)->bool:
		"""
		Проверяет литеру равно в импорте модулей. Может и не быть
		В словаре слов-- это по счёту ВТОРОЕ слово
		"""
		бРезульт :bool= False
		слово_равно :тСлово= сам.слова_секции[1]
		#строка_равно :str= слово_равно.Проверить()
		if слово_равно.род == тСлово.кПрисвоить: # есть уравнивание
			бРезульт = True
		return бРезульт

	def __Имя_Проверить(сам)->None:
		"""
		Пока не встретится "," или ";" -- заполнять имя алиаса
		"""
		def Имя_Проверить():
			"""
			Проверяет чтобы имя было строгим
			"""
			строка :str= слово_имя.строка
			бУсл1 :bool= слово_имя.ЕслиИмя_Строго() or (строка == ".")
			бУсл2 :bool= (строка !=",") and (строка !=";")
			return бУсл1 and бУсл2
		слово_имя :тСлово= сам.слова_секции[0]
		while Имя_Проверить():
			сам.__СловаСекции_Обрезать()
			сам.__имя += слово_имя.строка
			слово_имя = сам.слова_секции[0]
		сам.__СловаСекции_Обрезать() # Откидываем завершающий разделитель

	def __СловаСекции_Обрезать(сам)->None:
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список :dict= {}
		for ключ in range(1, len(сам.слова_секции)):
			новый_список[ключ-1]=сам.слова_секции[ключ]
		сам.слова_секции = {}
		сам.слова_секции = новый_список

	def Паспорт_Печать(сам)->None:
		"""
		Печатает паспорт модуля со всеми атрибутами.
		"""
		сам.__конс.Печать("\n+ Модуль:", сам.__имя)
		if сам.__стрАлиас != "":
			сам.__конс.Печать("|   Алиас \"" + сам.__имя + "\" :=", сам.__алиас_слово.строка)
		сам.__конс.Печать("+"+"-"*35)

	@property
	def стрАлиас(сам)->str:
		return сам.__стрАлиас

	@property
	def имя(сам)->str:
		return сам.__имя

	@property
	def бАлиас(сам)->bool:
		бАлиас = False
		if сам.__стрАлиас != "":
			бАлиас = True
		return бАлиас
