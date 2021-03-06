# coding:utf8
"""
Модуль разбора процедур.
"""
if True:
	#from . модПроцедура import тПроцедура
	from пакОберон.пакКомпилятор.пакСущность.пакСекция import тСекцияПроц
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакОшибка import тОшибка

class тСканерПроцедуры(тСекцияПроц):
	__slots__ = ("__конс", "ош_п", "__проц")
	def __init__(сам, пОберон, пДанные:dict)->None:
		сам.__конс = пОберон.конс
		сам.__конс.Отладить("тСканерПроцедуры.__init__()")

		сам.ош_п = тОшибка(пОберон, "тСканерПроцедуры")

		тСекцияПроц.__init__(сам, пОберон, пДанные)
		if сам.ошп.бВнутр:
			сам.ош_п.Внутр("__init__()", "При создании тСекцияПроц")
		сам.__проц :dict= {} # словарь по каждой глобальной процедуре в модуле
		сам.__Обработать()

	def __Обработать(сам)->None:
		"""
		Проводит разбор секции VAR.
		"""
		сам.__КонецПроц_Получить()
		if сам.ош_п.бИсх:
			сам.ош_п.Исх("__Обработать()", "При получении конца процедуры")
			return
		сам.СловаСекции_Получить()

	def __КонецПроц_Получить(сам)->None:
		"""
		Особенность в том, что нужно контролировать начало процедуры и её конец.
		Доказательство начала: __ PROCEDURE <имя> __
		Доказательство окончания __ END <имя>; __
		Нужно искать  END <имя>;  с конца
		"""
		цКонец :int= сам.цСловаМодуля - 1
		while цКонец >= 0:
			слово0 :тСлово= сам.слова_модуля[цКонец]
			if слово0.строка ==";":
				слово1 :тСлово= сам.слова_модуля[цКонец-1]
				if слово1.ЕслиИмя_Строго():
					слово2 :тСлово= сам.слова_модуля[цКонец-2]
					if слово2.строка == "END": # это точно конец процедуры
						break
			цКонец -= 1
		else:
			сам.ош_п.Исх("__КонецПроц_Получить()", "Нет конца процедуры")
			return
		сам.Конец_Уст(сам.слова_модуля[цКонец])
