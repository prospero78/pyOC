# coding: utf8
"""
Модуль "модПеременные".
Пакет содержит в себе определение секции переменных.
"""

if True:
	from пакКомпилер.пакСлово import тСлово
	from пакКомпилер.пакМодуль.пакПоле.модПоле import тПоле
	from пакКомпилер.пакМодуль.пакТипы.модРод import тРод
	from пакКомпилер.пакМодуль.пакСекция import тСекция

class тПеременные(тСекция):
	def __init__(сам, пДанные):
		тСекция.__init__(сам, пДанные)
		сам.__бПеремНеПустые = False # Есть ли переменные в секции
		сам.__перем = {} # словарь по словам каждой глобальной переменной в модуле
		сам.__Обработать()

	def __Слово_VAR_Обрезать(сам):
		"""
		Первое слово в списке слов должно быть VAR.
		Если нет -- значит в исходнике нет описания переменных.
		Возвращает результат встречи с VAR
		"""
		слово = сам.слова_модуль[0]
		if слово.строка =='VAR':
			# укоротить типы
			слова = {}
			for счёт in range(1, len(сам.слова_модуль)):
				слово = сам.слова_модуль[счёт]
				слово.Номер_Уст(счёт-1)
				слова[счёт-1] = слово
			сам.слова_модуля = {}
			сам.слова_модуля = слова
			сам.бСекцияЕсть = True
		return сам.бСекцияЕсть

	def __ЕслиПеремНеПустые(сам):
		"""
		Может быть следующее слово после окончания секции:   PROCEDURE BEGIN (* END модуля уже отброшено *)
		Секция VAR не может быть пустой, но если есть типы, они должны заканчиваться на ;
		"""
		def Слово_Проверить():
			бУсл = (type(слово) == тСлово)
			стрОш = "Слово должно быть тСлово, type=" + str(type(слово))
			assert бУсл, стрОш

		слово = сам.слова_модуль[0] # первое слово после VAR, а сам VAR уже распознан и отброшен
		Слово_Проверить()

		# проверим на внезапный конец секции
		бМаркер = (слово.строка in ["PROCEDURE", "BEGIN"])
		if not бМаркер: # секция переменных не пустая
			сам.__бПеремНеПустые = True
		return сам.__бПеремНеПустые

	def __ЕслиПеремОграничены(сам):
		"""
		Ищет разделитель окончания переменных.
		Сканируем слова все подряд.
		Может быть следующее слово-маркер окончания секции типов: PROCEDURE BEGIN,
		Первое слово всегда должен быть именем переменной и не может быть маркером
		Произвольное слово может быть ";" и не может быть маркером
		"""
		def Слово_Проверить():
			бУсл = type(слово) == тСлово
			стрОш = "тПеременные: Слово должно быть тСлово, type=" + str(type(слово))
			assert бУсл, стрОш
		def Маркер():
			сам.__бМаркер = (слово.строка in ["PROCEDURE", "BEGIN"])
		цСловМодульВсего = len(сам.слова_модуль) - 1 # отсчёт начинается с нуля
		цСловоСчёт = 0 # первый слово после VAR, а сам VAR уже распознали и отбросили
		слово = сам.слова_модуль[цСловоСчёт]
		Слово_Проверить()
		Маркер()
		while (not сам.__бМаркер) and (цСловоСчёт < цСловМодульВсего ):
			цСловоСчёт += 1
			слово = сам.слова_модуль[цСловоСчёт]

			Слово_Проверить()
			Маркер()
		цСловоСчёт -= 1
		слово = сам.слова_модуль[цСловоСчёт]
		сам.слово_конец = слово
		# Проверка на окончание секции типов
		if слово.строка != ";":
			сам.ошибка.Печать("тПеременные: слово ограничение секции типов должно быть ';', слово= " + слово.строка)

	def __Перем_Разделить(сам):
		"""
		Пока не исчерпаны слова секции -- последовательно вызываем новый тип.
		"""
		while len(сам.слова_секции) > 0:
			парам = {}
			парам['секция'] = сам
			парам['слова'] = сам.слова_секции
			перем = None
			перем = тПоле(парам)
			#перем.Паспорт_Печать()
			сам.слова_секции = {}
			сам.слова_секции = перем.слова_секции
			сам.__перем[len(сам.__перем)] = перем

	def __Обработать(сам):
		"""
		Проводит разбор секции VAR.
		"""
		if сам.__Слово_VAR_Обрезать():
			pass # "Есть переменные!")
		if сам.__ЕслиПеремНеПустые():
			pass # "Переменные не пустые!")
			#сам.__Перем_Печать()
			сам.__ЕслиПеремОграничены()
			#сам.Перем_Печать()
			сам.СловаСекции_Получить()
			#сам.Перем_Печать()
			сам.__Перем_Разделить()
			#сам.СловаСекции_Печать()

	def СловаСекции_Обрезать(сам):
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список = {}
		for ключ in range(1, len(сам.слова_секции)):
			новый_список[ключ-1]=сам.слова_секции[ключ]
		сам.слова_секции = {}
		сам.слова_секции = новый_список

	def Элемент_Проверить(сам, пПоле):
		"""
		Проверяет предка записи. Должно быть разрешённой строкой и
		не должно быть END.
		Кроме того, имя может быть составным
		"""
		стрОш = "тПеременные: тип элемента переменной должен быть допустимым именем, имя="
		слово_имя = сам.слова_секции[0]
		имя = слово_имя.Проверить()

		assert слово_имя.ЕслиСтр_Допустимо(), стрОш + имя
		assert пПоле.поле.массив_тип == тРод.сБезТипа, "тПоле: элемент массива уже назначен, элемент=" + сам.массив_тип
		элемент = ""
		while (имя == ".") or (слово_имя.ЕслиСтр_Допустимо()):
			сам.СловаСекции_Обрезать()
			элемент += имя
			слово_имя = сам.слова_секции[0]
			имя = слово_имя.Проверить()
		return элемент
