# coding:utf8
"""
Модуль описывает тип-запись.
"""

if True:
	from пакКомпилер.пакСлово import тСлово
	from пакКомпилер.пакМодуль.пакТипы.модРод import тРод
	from пакКомпилер.пакМодуль.пакПоле.модПоле import тПоле

class тТипЗапись:
	def __init__(сам, пДанные):
		сам.секция = пДанные['секция']
		сам.слова_секции = пДанные['слова']
		сам.поля = {} # все поля внутри записи
		сам.__Запись_Проверить()
		сам.__Поля_Проверить()
		сам.__Конец_Обрезать()

	def __Запись_Проверить(сам):
		"""
		Проверяет заголовок записи.
		Если есть предок -- заполняет предка.
		"""
		def СловоЗапись_Получить():
			слово_запись = сам.секция.слова_секции[0]
			строка_запись = слово_запись.Проверить()
			if строка_запись != "RECORD":
				assert False, "тТипЗапись: пропущено ключевое слово RECORD?"+слово_запись.стрИсх
			сам.секция.СловаСекции_Обрезать()
		def СкобкаЛевая_Обрезать():
			"""
			В этой позиции может быть скобка, а может и нет. Надо проверять.
			"""
			бРезультат = False
			слово_скобка = сам.секция.слова_секции[0]
			строка_скобка = слово_скобка.Проверить()
			if строка_скобка == "(":
				бРезультат = True
				сам.секция.СловаСекции_Обрезать()
			return бРезультат
		def СкобкаПрав_Обрезать():
				слово_скобка = сам.секция.слова_секции[0]
				строка_скобка = слово_скобка.Проверить()
				if строка_скобка != ")": # закрытие имени предка
					assert False, "тТипЗапись: пропущена закрывающая скобка предка?"+слово_скобка.стрИсх
				сам.секция.СловаСекции_Обрезать()
		СловоЗапись_Получить()
		if СкобкаЛевая_Обрезать():
			сам.секция.Предок_Проверить()
			СкобкаПрав_Обрезать()

	def __Поля_Проверить(сам):
		"""
		В записях ВСЕГДА встречается окончание "END" даже без
		вложенных полей.
		Поэтому здесь проверяем в цикле все поля, пока не закончатся
		"""
		слово_конец = сам.секция.слова_секции[0]
		строка_конец = слово_конец.Проверить()

		# если типы не встроенные (у встроенных типов нет полей)
		while строка_конец != "END": # нет окончания описания типа
			парам = {}
			парам['секция'] = сам
			парам['слова']  = сам.слова_секции
			сам.секция.поля[len(сам.секция.поля)] = тПоле(парам)
			слово_конец = сам.секция.слова_секции[0]
			строка_конец = слово_конец.Проверить()

	def __Конец_Обрезать(сам):
		"""
		Здесь может встретиться только одно слово: "END".
		"""
		слово_конец = сам.секция.слова_секции[0]
		строка_конец = слово_конец.Проверить()
		if строка_конец == "END": # есть окончание
			сам.секция.СловаСекции_Обрезать()
		else:
			assert False, "Слово окончания типа должно быть 'END'" + слово_конец.стрИсх
