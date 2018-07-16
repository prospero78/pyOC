# coding:utf8
"""
Модуль разбора процедур.
"""

class тПроцедуры:
	def __init__(сам, пКорень, пСловаМодуля):
		def Слова_Проверить():
			бУсл = type(пСловаМодуля) == dict
			стрОш = "В секцию процедур должен передаваться словарь слов, type=" + str(type(пСловаМодуля))
			пКорень.конс.Проверить(бУсл, стрОш)
		сам.__корень = пКорень
		Слова_Проверить()
		сам.__слова_модуль = пСловаМодуля
		сам.__слово_конец = None
		сам.слова_секции = {} #  Все пСлова секции процедур
		сам.__проц = {} # словарь по каждой глобальной процедуре в модуле
		сам.__бПроцЕсть = False # По умолчанию процедур нет
		сам.ошибка = пКорень.ошибка

	def __КонецПроц_Получить(сам):
		"""
		Особенность в том, что нужно контролировать начало процедуры и её конец.
		Доказательство начала: PROCEDURE <имя>(
		Доказательство окончания END <имя>;
		Нужно искать  END <имя>;  с конца
		"""
		цКонец = len(сам.__слова_модуль) - 1
		слово0 = None
		слово1 = None
		слово2 = None
		while цКонец >= 0:
			слово0 = сам.__слова_модуль[цКонец]
			if слово0.строка ==";":
				слово1 = сам.__слова_модуль[цКонец-1]
				if слово1.ЕслиИмя():
					слово2 = сам.__слова_модуль[цКонец-2]
					if слово2.строка == "END": # это точно конец процедуры
						print("Есть конец процедур!")
						break
			цКонец -= 1
		сам.__слово_конец = сам.__слова_модуль[цКонец + 2]
		print("Окончание процедур:", сам.__слово_конец)

	def __СловаСекции_Получить(сам):
		"""
		Выбирает слова по секции процедур.
		Дальше работает только с ними.
		"""
		слова_секции = {}  # будущий словарь слов секции процедур
		for цСчётПроц in range(0, сам.__слово_конец.номер - 1):
			слово = сам.__слова_модуль[цСчётПроц]
			слово._Номер_Уст(цСчётПроц)
			print("пр+", слово)
			слова_секции[цСчётПроц] = слово
		сам.слова_секции = слова_секции

		слова_модуля = {}  # будущий словарь слов модуля
		цСчётМодуль = 0
		for цСчёт in range(сам.__слово_конец.номер+1, len(сам.__слова_модуль)):
			слово = сам.__слова_модуль[цСчёт]
			слово._Номер_Уст(цСчётМодуль)
			#print("т-", цСчёт, слово.номер, слово.слово)
			слова_модуля[цСчётМодуль] = слово
			цСчётМодуль += 1
		сам.__слова_модуль = {}
		сам.__слова_модуль = слова_модуля

	def __Процедуры_Разделить(сам):
		"""
		Пока не исчерпаны слова секции -- последовательно вызываем новый тип.
		"""
		while len(сам.слова_секции) > 0:
			print("Слов проц=", len(сам.слова_секции))
			проц = None
			проц = тПроц(сам, None)
			проц.Паспорт_Печать()
			сам.__проц[len(сам.__проц)] = проц

	def СловаМодуля_Печать(сам):
		сам.__корень.конс.Печать("\nтПроцедуры.СловаМодуля_Печать()")
		for ключ in сам.__слова_модуль:
			слово = сам.__слова_модуль[ключ]
			сам.__корень.конс.Печать(слово)

	def СловаСекции_Печать(сам):
		print("Секция процедур ==========================================")
		сам.__корень.конс.Печать("\nпПроцедурф.СловаСекции_Печать()")
		for ключ in сам.слова_секции:
			слово = сам.слова_секции[ключ]
			сам.__корень.конс.Печать(слово.строка)

	def Обработать(сам):
		"""
		Проводит разбор секции VAR.
		"""
		сам.__КонецПроц_Получить()
		сам.__СловаСекции_Получить()
		#сам.Перем_Печать()
		сам.__Процедуры_Разделить()
		сам.СловаСекции_Печать()
