# coding: utf8
"""
Модуль определяет разбор секции типов.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from .модТип import тТип
	from пакОберон.пакКомпилятор.пакСущность.пакСекция import тСекцияТипы

class тТипы(тСекцияТипы):
	def __init__(сам, пДанные):
		тСекцияТипы.__init__(сам, пДанные)
		сам.__типы = {} # словарь по словам каждого типа в модуле
		сам.__бТипыНеПустые = False # По умолчанию секция TYPE пустая
		сам.__Обработать()


	def __ЕслиТипыНеПустые(сам):
		"""
		Может быть следующее слово:   ; VAR PROCEDURE BEGIN (* END модуля уже отброшено *)
		Секция TYPE может быть пустой, но если есть типы, они должны заканчиваться на ;
		"""
		def Слово_Проверить():
			бУсл = (type(слово) == тСлово)
			стрОш = "Слово должно быть тСлово, type=" + str(type(слово))
			assert бУсл, стрОш

		слово = сам.слова_модуля[0] # первое слово после TYPE, а сам TYPE уже распознан и отброшен
		Слово_Проверить()

		# проверим на внезапный конец секции
		бМаркер = (слово.строка in ["VAR", "PROCEDURE", "BEGIN"])
		if not бМаркер: # секция типизации не пустая
			сам.__бТипыНеПустые = True
		return сам.__бТипыНеПустые

	def __ЕслиТипыОграничены(сам):
		"""
		Ищет разделитель окончания типов.
		Сканируем слова все подряд.
		Может быть следующее слово-маркер окончания секции типов: VAR PROCEDURE BEGIN,
		так как типов может быть несколько, то ";" не подходит
		Первое слово всегда должен быть именем типа и не может быть маркером
		Произвольное слово может быть ";" и не может быть маркером
		"""
		def Слово_Проверить():
			бУсл = type(слово) == тСлово
			стрОш = "тТипы: Слово должно быть тСлово, type=" + str(type(слово))
			assert бУсл, стрОш
			# проверяем на предварительно равно -- тогда это не ограничитель
			if слово.строка == "PROCEDURE":
				слово1 = сам.слова_модуля[цСловоСчёт-1]
				if слово1.строка == "=":
					стрПроц = "процедура как тип"
				else:
					стрПроц = "PROCEDURE" # если нет скобки -- точно процедура как блок
			else:
					стрПроц = "вообще не процедура"

			# проверяем на предварительную скобку -- тогда это не ограничитель
			if слово.строка == "VAR":
				слово1 = сам.слова_модуля[цСловоСчёт-1]
				if слово1.строка == "(":
					стрПерем = "параметры процедур-типов"
				else:
					стрПерем = "VAR" # если нет скобки -- точно переменные как блок
			else:
					стрПерем = "вообще не переменные"

			сам.__бМаркер = (слово.строка in [стрПерем, стрПроц, "BEGIN"])

		цСловоСчёт = 0 # первый слово после TYPE, а сам TYPE уже распознали и отбросили
		слово = сам.слова_модуля[цСловоСчёт]
		сам.__бМаркер = False
		Слово_Проверить()
		while  цСловоСчёт < сам.цСловаМодуля - 1:
			if (not сам.__бМаркер):
				цСловоСчёт += 1
				слово = сам.слова_модуля[цСловоСчёт]
				Слово_Проверить()
			else:
				break
		слово = сам.слова_модуля[цСловоСчёт - 1]
		сам.Конец_Уст(слово)
		# Проверка на окончание секции типов
		assert слово.строка == ";", "тТипы: слово ограничение секции типов должно быть ';'" + слово.стрИсх

	def __Типы_Разделить(сам):
		"""
		Пока не исчерпаны слова секции -- последовательно вызываем новый тип.
		"""
		while len(сам.слова_секции) > 1:
			парам={}
			парам['секция'] = "TYPE"
			парам['слова']  = сам.слова_секции
			парам['имя'] = ""
			парам['бЭкспорт'] = False

			тип = None
			тип = тТип(парам)
			сам.__типы[len(сам.__типы)] = тип

			сам.слова_секции = {}
			сам.слова_секции = тип.слова_секции

	def __Обработать(сам):
		"""
		Проводит разбор секции TYPE.
		"""
		if сам.__ЕслиТипыНеПустые():
			pass # print("Типы не пустые!")
			#сам.Теги_Печать()
			сам.__ЕслиТипыОграничены()
			#сам.Теги_Печать()
			сам.СловаСекции_Получить()
			#сам.СловаСекции_Печать()
			#сам.Конст_Печать()
			#сам.__Типы_Разделить()
