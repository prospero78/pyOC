# coding:utf8
"""
Модуль описывает тип-запись.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод
	from пакОберон.пакКомпилятор.пакСущность.пакПоле import тПоле
	from . модТипБазовый import тТипБазовый

class тТипЗапись(тТипБазовый):
	def __init__(сам, пДанные):
		тТипБазовый.__init__(сам, пДанные)
		сам.поля = {} # все поля внутри записи
		сам.__СловоЗапись_Проверить()
		сам.__Запись_Проверить()
		if сам.__СкобкаЛевая_Обрезать():
			сам.Предок_Проверить()
			сам.__СкобкаПрав_Обрезать()
		сам.__Поля_Проверить()
		сам.__Конец_Обрезать()

	def __СловоЗапись_Проверить():
		слово_запись = сам.слова_секции[0]
		строка_запись = слово_запись.Проверить()
		if строка_запись != "RECORD":
			assert False, "тТипЗапись: пропущено ключевое слово RECORD?"+слово_запись.стрИсх
		сам.СловаСекции_Обрезать()

	def __СкобкаЛевая_Обрезать():
		"""
		В этой позиции может быть скобка, а может и нет. Надо проверять.
		"""
		бРезультат = False
		слово_скобка = сам.слова_секции[0]
		строка_скобка = слово_скобка.Проверить()
		if строка_скобка == "(":
			бРезультат = True
			сам.СловаСекции_Обрезать()
		return бРезультат

	def __СкобкаПрав_Обрезать():
		слово_скобка = сам.слова_секции[0]
		строка_скобка = слово_скобка.Проверить()
		if строка_скобка != ")": # закрытие имени предка
			assert False, "тТипЗапись: пропущена закрывающая скобка предка?"+слово_скобка.стрИсх
		сам.СловаСекции_Обрезать()

	def __Поля_Проверить(сам):
		"""
		В записях ВСЕГДА встречается окончание "END" даже без
		вложенных полей.
		Если вложенных полей нет -- значит разбор полей не вызываем.
		Поэтому здесь проверяем в цикле все поля, пока не закончатся
		Внутри типа-записи могут быть поля-записи.
		Если до END встречается RECORD -- значит счётчик END надо увеличивать.
		"""
		слово_конец = сам.слова_секции[1]
		строка_конец = слово_конец.Проверить()
		if not (строка_конец != "END"): # если запись не пустая
			слово_конец = сам.слова_секции[0]
			print("модТипЗапись стр.67, слово конец:", слово_конец.стрИсх)
			строка_конец = слово_конец.Проверить()
			# если типы не встроенные (у встроенных типов нет полей)
			цСчётКонец = 1
			цСчётСлово = 1
			while цСчётКонец > 0: # нет окончания описания типа
				парам = {}
				парам['секция'] = сам
				парам['слова']  = сам.слова_секции
				print("test")
				сам.поля[len(сам.поля)] = тПоле(парам)
				слово_конец = сам.слова_секции[цСчётСлово]
				строка_конец = слово_конец.Проверить()
				print("Стр.80", цСчётСлово, слово_конец)
				цСчётСлово += 1
				if строка_конец == "RECORD": # поле с записью
					цСчётКонец += 1
				elif строка_конец == "END": # закончилось либо поле, либо тип
					цСчётКонец -= 1
					assert  цСчётКонец < 0, "тТипЗапись: Сбой счётчика окончания END" +слово_конец.стрИсх
			сам.__слово_конец = слово_конец
		else:
			сам.__слово_конец = слово_конец
		print("модТипЗапись стр.91, слово конец:", сам.__слово_конец.стрИсх)

	def __Конец_Обрезать(сам):
		"""
		Здесь может встретиться только одно слово: "END".
		"""
		слово_конец = сам.слова_секции[0]
		строка_конец = слово_конец.Проверить()
		if строка_конец == "END": # есть окончание
			сам.СловаСекции_Обрезать()
		else:
			assert False, "тТипЗапись: Слово окончания типа должно быть 'END'" + слово_конец.стрИсх
