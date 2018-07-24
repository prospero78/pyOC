# coding:utf8
"""
Модуль описывает тип-массив.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод
	from . модАнализТипБазовый import тАнализТипБазовый

class тАнализТипМассив(тАнализТипБазовый):
	def __init__(сам, пДанные):
		тАнализТипБазовый.__init__(сам, пДанные)
		сам.род = "ARRAY"
		сам.элем = тРод.сБезТипа # элементы массива
		 # определяет число размерностей массива и их содержание
		сам.массив_размерность = {}
		сам.__МАССИВ_Обрезать()
		сам.__Массив_Проверить()
		сам.__Из_Обрезать()
		сам.Предок_Проверить()
		сам.Разделитель_Обрезать()

	def __МАССИВ_Обрезать(сам):
		слово_массив = сам.слова_секции[0]
		строка = слово_массив.Проверить()
		if строка != "ARRAY":
			assert False, "тАнализТипМассив: пропущено ARRAY?"+слово_массив.стрИсх
		сам.СловаСекции_Обрезать()

	def __Массив_Проверить(сам):
		"""
		Пытается проверить, является ли тип массивом.
		"""
		def Размерности_Получить():
			"""
			Рекурсивно получает и заполняет размерности массива.
			"""
			# получаем первую размерность массива
			слово_размер = сам.слова_секции[0]
			размер = int(слово_размер.Проверить())
			сам.массив_размерность[len(сам.массив_размерность)] = размер
			сам.СловаСекции_Обрезать()
			# есть ли ещё размерности
			слово_запятая = сам.слова_секции[0]
			запятая = слово_запятая.Проверить()
			if запятая == ",": # есть ещё размерности
				сам.СловаСекции_Обрезать()
				Размерности_Получить()
		Размерности_Получить()

	def __Из_Обрезать(сам):
		"""
		Образает OF (ARRRAY ... OF ... ;)
		"""
		слово_из = сам.слова_секции[0]
		строка = слово_из.Проверить()
		if строка != "OF":
			assert False, "тАнализТипМассив: пропущено OF в определении массива?" + слово_из.стрИсх
		сам.СловаСекции_Обрезать()
