# coding: utf8
"""
В секции TYPE анализирует поле ARRAY в записи
"""
if True:
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод
	from .модАнализТипПолеБазовый import тАнализТипПолеБазовый

class тАнализТипПолеМассив(тАнализТипПолеБазовый):
	def __init__(сам, пДанные):
		тАнализТипПолеБазовый.__init__(сам, пДанные)
		сам.род = "ARRAY"
		сам.элем = тРод.сБезТипа # элементы массива
		# определяет число размерностей массива и их содержание
		сам.массив_размерность = {}

		сам.ИмяПоле_Проверить()
		сам.бЭкспорт_Проверить()
		сам.Двоеточие_Обрезать()
		сам.__МАССИВ_Обрезать()
		сам.__Массив_Проверить()
		сам.__ИЗ_Обрезать()
		сам.__Элем_Проверить()
		сам.Разделитель_Обрезать()

	def __МАССИВ_Обрезать(сам):
		слово_массив = сам.слова_секции[0]
		строка = слово_массив.Проверить()
		if строка != "ARRAY":
			assert False, "тАнализЗаписьПолеМассив: пропущено ARRAY?"+слово_массив.стрИсх
		сам.СловаСекции_Обрезать()

	def __Массив_Проверить(сам):
		"""
		Пытается проверить, является ли поле массивом.
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

	def __ИЗ_Обрезать(сам):
		"""
		Образает OF (ARRRAY ... OF ... ;)
		"""
		слово_из = сам.слова_секции[0]
		строка = слово_из.Проверить()
		if строка != "OF":
			assert False, "тАнализЗаписьПолеМассив: пропущено OF в определении массива?" + слово_из.стрИсх
		сам.СловаСекции_Обрезать()

	def __Элем_Проверить(сам):
		"""
		Проверяет предка поля. Должно быть разрешённой строкой
		Кроме того, имя может быть составным
		У полей два разделителя -- ";" или "END"
		===== Улучшенная проверенная версия =======
		"""
		слово_имя = сам.слова_секции[0]
		имя = слово_имя.Проверить()
		стрОш = "тАнализТипПолеБазовый: имя типа должно быть допустимым именем"
		assert слово_имя.ЕслиСтр_Допустимо(), стрОш + слово_имя.строка + слово_имя.стрИсх
		if сам.элем != тРод.сБезТипа:
			assert False, "тАнализТипБазовый: элемент массива уже назначен  " + сам.элем + слово_имя.стрИсх
		сам.элем = ""
		while (имя == ".") or (слово_имя.ЕслиСтр_Допустимо()):
			# Такое может быть в определении 1) массива 2) предка записи
			if имя == ";" or имя =="END":
				сам.СловаСекции_Обрезать()
				break
			if not (слово_имя.ЕслиСтр_Допустимо() or имя=="."):
				assert False, стрОш + слово_имя.строка + слово_имя.стрИсх
			сам.СловаСекции_Обрезать()
			сам.элем += имя
			слово_имя = сам.слова_секции[0]
			имя = слово_имя.Проверить()
