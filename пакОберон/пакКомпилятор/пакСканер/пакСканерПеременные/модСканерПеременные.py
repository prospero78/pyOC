# coding: utf8
"""
Модуль "модПеременные".
Пакет содержит в себе определение секции переменных.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакСекция import тСекцияПерем

class тСканерПеременные(тСекцияПерем):
	def __init__(сам, пДанные):
		тСекцияПерем.__init__(сам, пДанные)
		сам.__бПеремНеПустые = False # Есть ли переменные в секции
		сам.__Обработать()

	def __Слово_VAR_Обрезать(сам):
		"""
		Первое слово в списке слов должно быть VAR.
		Если нет -- значит в исходнике нет описания переменных.
		Возвращает результат встречи с VAR
		"""
		слово = сам.слова_модуля[0]
		if слово.строка =='VAR':
			# укоротить типы
			сам.СловаСекции_Обрезать()
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

		слово = сам.слова_модуля[0] # первое слово после VAR, а сам VAR уже распознан и отброшен
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
		def УслСтоп():
			слово = сам.слова_модуля[цСловоСчёт]
			бУсл = type(слово) == тСлово
			стрОш = "тПеременные: Слово должно быть тСлово, type=" + str(type(слово))
			assert бУсл, стрОш
			строка = слово.строка
			if строка == "PROCEDURE":
				бСтоп1 = True
			elif строка == "BEGIN":
				бСтоп1 = True
			else:
				бСтоп1 = False
			#бСтоп1 = (слово.строка in ["PROCEDURE", "BEGIN"])
			бСтоп2 = (цСловоСчёт < цСловМодульВсего)
			return бСтоп1 and бСтоп2

		цСловМодульВсего = сам.цСловаМодуля - 1 # отсчёт начинается с нуля
		цСловоСчёт = 0 # первый слово после VAR, а сам VAR уже распознали и отбросили

		while not УслСтоп():
			цСловоСчёт += 1
			слово = сам.слова_модуля[цСловоСчёт]

		цСловоСчёт -= 1
		слово = сам.слова_модуля[цСловоСчёт]
		сам.Конец_Уст(слово)
		# Проверка на окончание секции типов
		assert слово.строка == ";", "тПеременные: слово ограничение секции VAR должно быть ';'" + слово.стрИсх

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
			#сам.__Перем_Разделить()
			#сам.СловаСекции_Печать()

	# def СловаСекции_Обрезать(сам):
		# """
		# Уменьшает слова секции на 1 с головы.
		# """
		# новый_список = {}
		# for ключ in range(1, len(сам.слова_секции)):
			# новый_список[ключ-1]=сам.слова_секции[ключ]
		# сам.слова_секции = {}
		# сам.слова_секции = новый_список

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

	def Парам_Получ(сам) -> dict:
		парам = {}
		парам['слова'] = сам.слова_модуля
		парам['слова_секции'] = сам.слова_секции
		return парам
