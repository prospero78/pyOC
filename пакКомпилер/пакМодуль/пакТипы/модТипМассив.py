# coding:utf8
"""
Модуль описывает тип-массив.
"""

if True:
	from пакКомпилер.пакМодуль.пакТипы.модРод import тРод

class тТипМассив:
	def __init__(сам, пТип):
		сам.тип = пТип
		сам.элем = тРод.сБезТипа
		сам.__Массив_Проверить()

	def __Массив_Проверить(сам):
		"""
		Пытается проверить, является ли тип массивом.
		"""
		def Размерности_Получить():
			"""
			Рекурсивно получает и заполняет размерности массива.
			"""
			# получаем первую размерность массива
			размер = int(сам.тип.Слово_Проверить())
			сам.тип.массив_размерность[len(сам.тип.массив_размерность)] = размер
			сам.тип.СловаСекции_Обрезать()
			# есть ли ещё размерности
			запятая = сам.тип.Слово_Проверить()
			if запятая == ",": # есть ещё размерности
				сам.тип.СловаСекции_Обрезать()
				Размерности_Получить()

		строка = сам.тип.Слово_Проверить()
		if строка == "ARRAY":
			сам.__род = тРод.сВстроен
			сам.тип.Предок_Уст("ARRAY")
			сам.тип.СловаСекции_Обрезать() # Обрезает "ARRAY"
			Размерности_Получить()
			# сейчас слово должно быть OF
			строка = сам.тип.Слово_Проверить()
			if строка != "OF":
				assert False, "тТип: пропущено OF в определении массива? слово=" + строка
			сам.тип.СловаСекции_Обрезать()
			# TODO: здесь надо убедиться, что имя типа элемента массива -- допустимое имя.
			строка_тип = сам.тип.Слово_Проверить()
			сам.тип.массив_тип = строка_тип
			сам.тип.СловаСекции_Обрезать()
			# Проверка разделителя происходит в тТип
			# # теперь ковыряем разделитель
			# # строка_раздел = сам.тип.Слово_Проверить()
			# # if строка_раздел != ";":
			# #	assert False, "тТипМассив: пропущен разделитель в определении массива? слово="+строка_раздел
